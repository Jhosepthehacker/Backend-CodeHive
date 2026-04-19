from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.status import HTTP_403_FORBIDDEN
import sqlmodel
import pysqlite3 as sql

class DataBase:
    def __init__(self, conn):
        try:
            self.conn = conn
            self.conn.commit()
            self.conn.close()
        except AttributeError:
            return 1

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

    def insert_data(self, user_name, last_name):
        try:
            self.conn = sql.connect("data_server.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"INSERT INTO users VALUES('{user_name}', '{last_name}', '{is_google}');") # Critical vulnerability: SQL Inyection
        finally:
            self.conn.commit()
            self.conn.close()

class Input(BaseModel):
    user_name: str

app = FastAPI(
    title="Backend CodeHive",
    description="This is my app Backend CodeHive"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post('/user_names', tags=["User Names"])
def recolect_name(user_name: str):
    conn = sql.connect("data_server.db")
    db = DataBase(conn)

    if db == 1:
        print("Error in DB")
        print("Code 1")

        return {
            "status": 500
        }
    
    else:
        try:
            db.insert_data(user_name, None, None)
        except NameError:
            print("NameError: code 1")

        return {
            "status": 201
        }

@app.post('/last_name_for_users', tags=["Last Name For Users"])
def recolect_last_name():
    return {
        "status": 201
    }

# @app.post('/is_google', tags=["Protect Server"])
# def is_google():
#
#
#     return {
#         "status": 403
#     }

# @app.post('/accounts', tags=["Accounts"])
# def login():
#     return {}

if __name__ == '__main__':
    conn = sql.connect("data_server.db")
    
    db = DataBase(conn)
