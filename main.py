
from fastapi import FastAPI
from router.router import user
#from router.router_ssn import ssn

app = FastAPI()

app.include_router(user, prefix="/v1/api/users", tags=["users"])
#app.include_router(ssn, prefix="/v1/api/ssion", tags=["session"])

# @app.get ("/")
# def root ():
#     return "hola estoy aqui"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

