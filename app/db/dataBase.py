from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:$2a$10$03NOBAUgnNH8nnTplWY2f.oWXn29wwDyd4RrrSy4X9aHwR1tNNx9m@47.115.205.23:3306/chat_vits", pool_size=15, max_overflow=30)
Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine
Session = sessionmaker(bind=engine)



