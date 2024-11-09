# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class RechargeConsumptionRecord(Base):
    __tablename__ = 'recharge_consumption_record'
    __table_args__ = {'comment': '充值消费记录表'}

    id = Column(Integer, primary_key=True, comment='ID')
    recharge = Column(DECIMAL(10, 2), nullable=False, comment='充值金额')
    consumption = Column(DECIMAL(10, 2), nullable=False, comment='消费金额')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    is_deleted = Column(TINYINT(1), server_default=text("'0'"), comment='是否删除')
    user_id = Column(Integer, nullable=False, comment='用户ID')