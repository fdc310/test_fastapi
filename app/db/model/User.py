# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, String, Text, text, func, Integer, Boolean, TIMESTAMP, Date
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'comment': '用户信息表'}

    userId = Column(Integer, primary_key=True, comment='用户ID')
    userAccount = Column(String(255), nullable=False, comment='用户账号')
    userPassword = Column(String(255), nullable=False, comment='用户密码')
    avatar = Column(String(255), comment='头像')
    isAccountActive = Column(TINYINT(1), comment='账号是否激活')
    accountValidity = Column(Date, comment='账号有效期')
    loginIP = Column(String(255), comment='登录IP')
    loginTime = Column(TIMESTAMP, comment='登录时间')
    createTime = Column(TIMESTAMP, comment='创建时间')
    userPoints = Column(Integer, comment='用户积分')
    userRemarks = Column(Text, comment='用户备注')
    parentId = Column(Integer, comment='父级ID')
    userLevel = Column(Integer, comment='用户等级')
    isDeleted = Column(TINYINT(1), comment='是否删除')