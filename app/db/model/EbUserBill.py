# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DECIMAL, INTEGER, MEDIUMINT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class EbUserBill(Base):
    __tablename__ = 'eb_user_bill'
    __table_args__ = (
        Index('type', 'category', 'type', 'link_id'),
        {'comment': '用户账单表'}
    )

    id = Column(INTEGER(10), primary_key=True, comment='用户账单id')
    uid = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"), comment='用户uid')
    link_id = Column(String(32), nullable=False, server_default=text("'0'"), comment='关联id')
    pm = Column(TINYINT(1), nullable=False, index=True, server_default=text("'0'"), comment='0 = 支出 1 = 获得')
    title = Column(String(64), nullable=False, server_default=text("''"), comment='账单标题')
    category = Column(String(64), nullable=False, server_default=text("''"), comment='明细种类')
    type = Column(String(64), nullable=False, server_default=text("''"), comment='明细类型')
    number = Column(DECIMAL(8, 2), nullable=False, server_default=text("'0.00'"), comment='明细数字')
    balance = Column(DECIMAL(16, 2), nullable=False, server_default=text("'0.00'"), comment='剩余')
    mark = Column(String(512), nullable=False, server_default=text("''"), comment='备注')
    status = Column(TINYINT(1), nullable=False, index=True, server_default=text("'1'"), comment='0 = 带确定 1 = 有效 -1 = 无效')
    create_time = Column(TIMESTAMP, index=True, server_default=text("CURRENT_TIMESTAMP"), comment='添加时间')
    update_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')
