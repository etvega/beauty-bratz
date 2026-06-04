from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routes.routes import router
import os

app = FastAPI(title="Beauty Bratz", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

templates = Jinja2Templates(directory="app/models/templates")

@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")