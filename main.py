from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def index(limit, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} publised blogs from the databse'}
    else:
        return {'data': f'{limit} blogs from the databse'}

@app.get('/blog/unpublished')
def unpublished():
    # fetch all unpublished blogs
    return {'data': 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog post {blog.title} was created'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)