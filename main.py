from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

myposts = []

# Define schema for post requests
class Post(BaseModel):
    title:str
    content:str
    published: bool = False
    rating: Optional[int] = None
    

# Path operation (route in flask)
@app.get("/")
def root():
    return {"message":"Hello FASTAPI"}

@app.get("/posts")
def get_posts():
    return {"data":myposts}


# To get objects from the body of post request
# @app.post("/createposts")
# def create_posts(payload:dict = Body(...)):
#     print(payload)
#     return {"message": "successfully posted"}

# Data that we want from the user
# Fastapi automatically validates the data front end sends us using the schema we defined
@app.post("/createposts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1,1000000)
    myposts.append(post_dict)
    return {"data":myposts}