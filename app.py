from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.status import HTTP_403_FORBIDDEN
import sqlmodel
import sqlite3 as sql

class DataBase:
    def __init__(self, conn):
        try:
            self.conn = conn
            self.conn.commit()
            self.conn.close()
        except AtributeError:
            pass

        self.create_table()

    def create_table(self):
        try:
            self.conn = sql.connect("data_server.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS users(
                     name TEXT,
                     last_name TEXT,
                     is_google TEXT
                )"""
            )
        finally:
            self.conn.commit()
            self.conn.close()

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

@app.post('/user_names', tags=["User Names"])
def name():
    
    
    return {
        "status": 201
    }

# @app.post('/accounts', tags=["Accounts"])
# def login():
#     return {}

if __name__ == '__main__':
    conn = sql.connect("data_server.db")
    db = DataBase(conn)
