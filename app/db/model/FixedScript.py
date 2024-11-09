from sqlalchemy import Column, DECIMAL, Date, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class FixedScript(Base):
    __tablename__ = 'fixed_script'
    __table_args__ = {'comment': '固定脚本表'}

    id = Column(Integer, primary_key=True, comment='ID')
    script_name = Column(String(255), nullable=False, comment='脚本名称')
    script_content = Column(Text, nullable=False, comment='脚本内容')
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    is_deleted = Column(TINYINT(1), server_default=text("'0'"), comment='删除标志')
    created_by = Column(String(255), comment='创建者')
    script_type = Column(Integer, comment='脚本类型')
