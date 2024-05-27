from sqlalchemy import create_engine, MetaData

engine=create_engine("mysql+pymysql://PLMV:Abc123.@127.0.0.1:3306/testtpvz")

#conn = engine.connect()

meta_data=MetaData()

