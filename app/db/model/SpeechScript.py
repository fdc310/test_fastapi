# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, String, Text, text, func, Integer, Boolean, TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class SpeechScript(Base):
    __tablename__ = 'speech_scripts'
    __table_args__ = {'comment': '生成话术信息表'}

    textId = Column(INTEGER(11), primary_key=True, comment='文本ID')
    userId = Column(INTEGER(11), comment='用户ID')
    scriptText = Column(Text, comment='话术文本')
    audioUrl = Column(String(255), comment='音频地址')
    createTime = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updateTime = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')
    txt_role = Column(String(255), comment='角色')
    consumption = Column(INTEGER(11), comment='消费')
    residual = Column(INTEGER(11), comment='剩余积分')
    isDeleted = Column(TINYINT(1), comment='删除')
    title = Column(String(255), comment='标题')