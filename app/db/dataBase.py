from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://usaename:password@47.115.205.23:3306/chat_vits", pool_size=15, max_overflow=30)
Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine
Session = sessionmaker(bind=engine)



