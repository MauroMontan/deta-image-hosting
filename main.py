from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
import src.images_controller as images
app:FastAPI = FastAPI()

app.include_router(images.router)

@app.get("/", response_class=HTMLResponse)
def render():
    return """
    <form action="/images/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>
    """
