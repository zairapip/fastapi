from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

session=Table ("tsessions", meta_data,
             Column ("id", Integer, primary_key=True),
             Column ("username", String (50), nullable=False),
             Column ("email", String (100), nullable=False, unique=True),
             Column ("token_access", String (255), nullable=False))

meta_data.create_all(engine)