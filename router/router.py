from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.user_schema import UserSchemaP, UserSchemaG
from config.db import engine
from model.users import tusers
from typing import List
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()

@user.get("/")
def root():
    return {"message":"Hola aqui estoy router"}

@user.get("/v1/api/users", response_model=List[UserSchemaG])
#def get_users(data_user: UserSchemaG):
def get_users():
    with engine.connect() as conn:
        result= conn.execute(tusers.select()).fetchall()
        print(result)
        return result

@user.get("/v1/api/users/{user_id}", response_model=UserSchemaG)
#def get_users(data_user: UserSchemaG):
def get_user(user_id:str):
    with engine.connect() as conn:
        result= conn.execute(tusers.select().where(tusers.c.id==int(user_id))).first()
        if result is not None:
            print(result)
            return result
        else:
            error_message = {"id":-1,
                             "name": "string",
                             "surname": "string",
                             "email": "string",
                             "password_hash": "string",
                             "username": "string",
                             "telephone": "string",
                             "ERROR": "No existe ningún usuario con ese ID"}
            return error_message

@user.post("/v1/api/register_user", status_code=HTTP_201_CREATED)
def create_users(data_user: UserSchemaP, status_code=HTTP_201_CREATED):
    #print (data_user)
    new_user= data_user.dict()
    new_user["password_hash"] = generate_password_hash(data_user.password_hash,"pbkdf2:sha256:30",30)
    #print (new_user)
    with engine.connect() as conn:
        conn.execute(tusers.insert().values(new_user))
        conn.commit()
        return Response (status_code=HTTP_201_CREATED)

@user.put("/v1/api/users/{user_id}", response_model=UserSchemaG)
#def get_users(data_user: UserSchemaG):
def put_user(user_id:str, data_update:UserSchemaP):
    new_user = data_update.dict()
    new_user["password_hash"] = generate_password_hash(data_update.password_hash, "pbkdf2:sha256:30", 30)

    with engine.connect() as conn:
        conn.execute(tusers.update().values(new_user).where(tusers.c.id == int(user_id)))
        conn.commit()

        result = conn.execute(tusers.select().where(tusers.c.id == int(user_id))).first()

        if result is not None:
            print(result)
            return result

@user.delete("/v1/api/users/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    with engine.connect() as conn:
        conn.execute(tusers.delete().where(tusers.c.id == int(user_id)))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)