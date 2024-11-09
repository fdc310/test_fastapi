# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, String, Text, text, func, Integer, Boolean, TIMESTAMP
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class SoundColor(Base):
    __tablename__ = 'sound_colors'
    __table_args__ = {'comment': '音色信息表'}

    soundColorId = Column(Integer, primary_key=True, comment='音色ID')
    soundColorName = Column(String(255), comment='音色名称')
    userId = Column(Integer, comment='用户ID')
    createTime = Column(TIMESTAMP, comment='创建时间')
    isDeleted = Column(TINYINT(1), comment='删除')
    updateTime = Column(TIMESTAMP, comment='更新时间')
    soundColorInfo = Column(Text, comment='音色信息')
    soundColorType = Column(String(255), comment='音色类型')
    category = Column(String(255), comment='分类')
    soundCharacterImage = Column(String(255), comment='音色人物图片')
    auditionSound = Column(String(255), comment='音色试听音')
    gender = Column(String(50), comment='性别')
    sovits_name = Column(String(255), comment='声音sovits模型')
    gpt_name = Column(String(255), comment='声音gpt模型')
    prompt_text = Column(String(255), comment='试听音频文本')