from sqlalchemy.schema import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

tusers=Table ("tusers", meta_data,
             Column ("id", Integer, primary_key=True),
             Column ("name", String (50), nullable=False),
             Column ("surname",String (50), nullable=False),
             Column ("email", String (100), nullable=False, unique=True),
             Column ("password_hash", String (255), nullable=False),
             Column ("username", String (200), nullable=False),
             Column ("telephone", String (16), nullable=False, default="555-55-55-55"))

meta_data.create_all(engine)