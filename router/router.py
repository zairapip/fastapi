import bcrypt
from fastapi import APIRouter, Response, Header
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.user_schema import UserSchemaP, UserSchemaG, UserSchemaE
from fastapi.responses import JSONResponse
#from schema.ssn_schema import SsnSchemaP, SsnSchemaG
from config.db import engine
from model.users import tusers
#from model.sessions import tsession
from typing import List, Union
from werkzeug.security import generate_password_hash, check_password_hash


#----------------+++++++++  Users  ++++++++++------------------------------


user = APIRouter()

@user.get("/")
def root():
    return {"message":"Hola aqui estoy router"}

@user.get("/gets/", response_model=List[UserSchemaG])
#def get_users(data_user: UserSchemaG):
def get_users():
    with engine.connect() as conn:
        result= conn.execute(tusers.select()).fetchall()
        print(result)
        return result

@user.get("/get/{user_id}", response_model=Union[UserSchemaG, UserSchemaE])
#def get_users(data_user: UserSchemaG):
def get_user(user_id:str, token:str=Header(...)):
    if token is not None:
        with engine.connect() as conn:
            check_token=conn.execute(tsession.select().where(tsession.c.token_a>
            if check_token:
                result= conn.execute(tusers.select().where(tusers.c.id==int(use>
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
            else:
                return {'error': 'Token is wrong'}
    else:
        return {'error': 'Token does not exist'}

@user.post("/register/", status_code=HTTP_201_CREATED)
def create_users(data_user: UserSchemaP, status_code=HTTP_201_CREATED):
    #print (data_user)
    new_user= data_user.dict()
    new_user["password_hash"] = generate_password_hash(data_user.password_hash,>
    #print (new_user)
    with engine.connect() as conn:
        conn.execute(tusers.insert().values(new_user))
        conn.commit()
        #return Response (status_code=HTTP_201_CREATED)
        return JSONResponse(content={"is_created": True}, status_code=201)

@user.put("/pu/{user_id}", response_model=UserSchemaG)
#def get_users(data_user: UserSchemaG):
def put_user(user_id:str, data_update:UserSchemaP):
    new_user = data_update.dict()
    new_user["password_hash"] = generate_password_hash(data_update.password_has>

    with engine.connect() as conn:
        conn.execute(tusers.update().values(new_user).where(tusers.c.id == int(>
        conn.commit()

        result = conn.execute(tusers.select().where(tusers.c.id == int(user_id)>
        
        if result is not None:
            print(result)
            return result

@user.delete("/er/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    with engine.connect() as conn:
        conn.execute(tusers.delete().where(tusers.c.id == int(user_id)))
        conn.commit()

        return Response(status_code=HTTP_204_NO_CONTENT)



