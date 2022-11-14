from fastapi import FastAPI, Request 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.auth.auth import Auth
import src.images_controller as images
app:FastAPI = FastAPI()

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="src/templates")

app.include_router(images.router)

@app.get("/users/{token}")
async def users(token:str):
    return Auth.currentUser(token)

@app.get("/", response_class=HTMLResponse)
def render(r:Request):
    return templates.TemplateResponse("index.html",{"request":r})
