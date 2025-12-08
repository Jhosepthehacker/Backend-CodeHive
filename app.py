from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.status import HTTP_403_FORBIDDEN
import json
import sqlmodel

class Input(BaseModel):
    user_name: str

app = FastAPI(
    title="My App Full-Stack",
    description="This is my app full-stack"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/welcome', tags=["Welcome"])
def message_of_welcome():
    return {
        "message": "Bienvenido(a) a mi app full-stack"
        }

@app.post('/accounts', tags=["Accounts"])
def login():
    return {
        "status": 201,
        "detail": "Created"
    }
