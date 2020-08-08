import os 

from sqlalchemy import (
    create_engine, MetaData,
    Column, DateTime, 
    Integer, MetaData, 
    String, Table,
)
from sqlalchemy.sql import func 

from databases import Database 

DATABASE_URL = "postgresql://postgres:root@localhost/hello_fastapi_dev"

engine = create_engine(DATABASE_URL)    
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

database = Database(DATABASE_URL)
