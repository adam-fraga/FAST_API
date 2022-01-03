from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

# !!!WARNING!!!
# Fast api read the first path request if that match the next are skip

app = FastAPI()


# Pydantic allow use to use Schema for our API to define the type of data we excepts from users
# Pydantic can also throw errors if the type not match
class Post(BaseModel):
    title: str
    content: str
    # Provide optionnal value if no value send default is True
    published: bool = True
    # Provide optionnal value of type int if no value send = None
    rating: Optional[int] = None


""" 
GET method
Arguments: Path to root
Returns: Python dictionnary convert to JSON
"""


@app.get('/')
def root():
    # Each time modify the return we have to relaunch uvicorn server
    # --reload allow uvicorn to watch changes
    return {"message": "Hello world!!"}


""" 
GET method
Arguments: Path to posts
Returns: Python dictionnary convert to JSON
"""


@app.get('/posts')
def method_name():
    return {"data": "This is your posts"}


""" 
POST method
Arguments: Path to posts
Returns: Python dictionnary convert to JSON
"""


@app.post('/posts')
# Stock Post data into a dictionnary variable named payLoad Body is import from Fastapi
# def create_post(payLoad: dict = Body(...)):
# display the data in uvicorn server
# print(payLoad)
# display the data in a python dictionnary (JSON)
# return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}
# OR with pydantic Model
# Post here reference our pydantic Model for our Post we except a content ant a title both (str)
# Here before the execution the moel is checked and it throws error for users to inform them of
# what data the API is excepting from them
def create_post(my_post: Post):
    # my_post is now an object of type post and allow us to access easly the data
    print(my_post.title)
    # Pydantic allow us to convert a Pydantic model to a dictionnary with dict method
    print(my_post.dict())
    return {"data": my_post}
