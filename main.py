from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

# !!!IMPORTANT!!!
# Fast api read the first path request if that match the next are skip.
# Each time modify the return we have to relaunch uvicorn server.
# --reload allow uvicorn to watch for changes.


app = FastAPI()

"""
PYDANTIC:
  Allow to use Schema for our API to define the type of data we excepts from users.
  Can also throw errors if the type not match.
  Convert the result into an object to facilite the access of the data.
  Provide à dict() Method to convert the object in a dictionnary.
"""


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# Post test (Substitute to table SQL)
my_posts = [{"title": "title of post 1",
             "content": "content of post 1", "id": 1},
            {"title": "title of post 2",
             "content": "content of post 2", "id": 2}]

"""
    Utilitie function (substitute to SQL select request )
"""


def find_post(id):
    return my_posts[id]


""" 
GET method
Arguments: Path to root
Returns: Python dictionnary convert to JSON
"""


@app.get('/')
def root():
    return {"message": "Hello world!!"}


""" 
GET method
Arguments: Path to posts
Returns: Python dictionnary convert to JSON
"""


@app.get('/posts')
def method_name():
    return {"data": my_posts}


""" 
POST method
arguments decorators: path to posts

!!!PREFERE EXAMPLE 2 WITH PYDANTICS!!!
arguments method (example 1): post = Catch the request body response convert it into a dictionnary
arguments method (example 2): post = Use Pydantics Model 

returns: python dictionnary convert to json

!!!NOTES!!!
(the printed value are displayed in uvicorn server)
(The return Value are displayed the data in a python dictionnary convert to JSON)
"""

# EXAMPLE 1
# @app.post('/posts')
# def create_post(post: dict = Body(...)):
#     print(post)
#     return {"new_post": f"title: {post['title']} content: {post['content']}"}


# EXAMPLE 2
@app.post('/posts')
def create_post(post: Post):
    # print(post.title)
    # print(post.dict())
    # We need an id for our post randrange provide is for us
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    # Append new post to my_posts (simulate BDD)
    my_posts.append(post_dict)
    return {"data": post_dict}


""" 
GET method
decorator arguments: path to posts
method arguments: id (automaticaly catch from the path)
returns: python dictionnary convert to JSON
"""


@app.get('/posts/{id}')
def get_post(id):
    return {"post": find_post(id)}
