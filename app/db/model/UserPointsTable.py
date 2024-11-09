# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class UserPointsTable(Base):
    __tablename__ = 'user_points_table'
    __table_args__ = {'comment': '用户积分表，时长以分钟计'}
    id = Column(Integer, primary_key=True, comment='ID')
    userId = Column(Integer, nullable=False, comment='用户ID')
    totalDuration = Column(Integer, comment='总时长(分钟)')
    consumedDuration = Column(Integer, comment='消费时长(分钟)')
    remainingDuration = Column(Integer, comment='剩余时长(分钟)')
    createTime = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updateTime = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')
    isDeleted = Column(TINYINT(1), server_default=text("'0'"), comment='删除标志')