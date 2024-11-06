from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "greeting": ""})

@app.post("/greet", response_class=HTMLResponse)
async def greet_user(request: Request, username: str = Form(...)):
    greeting_message = f"Добро пожаловать, {username}!"
    return templates.TemplateResponse("index.html", {"request": request, "greeting": greeting_message})

