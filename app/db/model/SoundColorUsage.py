
# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, String, Text, text, func, Integer, Boolean, TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata





class SoundColorUsage(Base):
    __tablename__ = 'sound_color_usage'
    __table_args__ = {'comment': '音色使用记录表'}

    id = Column(Integer, primary_key=True, comment='记录ID')
    userId = Column(Integer, comment='用户ID')
    soundColorId = Column(Integer, comment='音色ID')
    usageTime = Column(TIMESTAMP, comment='使用时间')