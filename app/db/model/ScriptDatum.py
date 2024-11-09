
from sqlalchemy import Column, DECIMAL, DateTime, String, Text, text, func, Integer, Boolean, TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ScriptDatum(Base):
    __tablename__ = 'script_data'
    __table_args__ = {'comment': '脚本数据表'}

    questionId = Column(Integer, primary_key=True, comment='问题ID')
    question = Column(Text, comment='问题')
    reply = Column(Text, comment='回复')
    analyzedReply = Column(Text, comment='解析回复')
    event = Column(String(255), comment='事件')
    userId = Column(Integer, comment='用户ID')
    createTime = Column(TIMESTAMP, comment='创建时间')
    updateTime = Column(TIMESTAMP, comment='更新时间')
    isDeleted = Column(TINYINT(1), comment='删除')
