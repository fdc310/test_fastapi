from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, DECIMAL, INTEGER, MEDIUMINT, SMALLINT, TINYINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:$2a$10$03NOBAUgnNH8nnTplWY2f.oWXn29wwDyd4RrrSy4X9aHwR1tNNx9m@47.115.205.23:3306/crmeb", pool_size=15, max_overflow=30)



Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine
Session = sessionmaker(bind=engine)

class EbUser(Base):
    __tablename__ = 'eb_user'
    __table_args__ = {'comment': '用户表'}

    user_id = Column(INTEGER(10), primary_key=True, comment='用户id')
    user_name = Column(String(32), nullable=False, unique=True, server_default=text("''"), comment='用户账号')
    password = Column(String(255), server_default=text("''"), comment='用户密码')
    real_name = Column(String(25), server_default=text("''"), comment='真实姓名')
    birthday = Column(String(32), server_default=text("''"), comment='生日')
    card_id = Column(String(20), server_default=text("''"), comment='身份证号码')
    mark = Column(String(255), server_default=text("''"), comment='用户备注')
    partner_id = Column(INTEGER(11), comment='合伙人id')
    group_id = Column(String(255), server_default=text("''"), comment='用户分组id')
    tag_id = Column(String(255), server_default=text("''"), comment='标签id')
    nickname = Column(String(255), server_default=text("''"), comment='用户昵称')
    avatar = Column(String(256), server_default=text("''"), comment='用户头像')
    phone = Column(CHAR(15), comment='手机号码')
    add_ip = Column(String(16), server_default=text("''"), comment='添加ip')
    last_ip = Column(String(16), server_default=text("''"), comment='最后一次登录ip')
    now_money = Column(DECIMAL(16, 2), server_default=text("'0.00'"), comment='用户余额')
    brokerage_price = Column(DECIMAL(8, 2), server_default=text("'0.00'"), comment='佣金金额')
    integral = Column(INTEGER(11), server_default=text("'0'"), comment='用户剩余积分')
    experience = Column(INTEGER(10), server_default=text("'0'"), comment='用户剩余经验')
    sign_num = Column(INTEGER(11), server_default=text("'0'"), comment='连续签到天数')
    level = Column(TINYINT(3), index=True, server_default=text("'0'"), comment='等级')
    spread_uid = Column(INTEGER(10), index=True, server_default=text("'0'"), comment='推广员id')
    spread_time = Column(TIMESTAMP, comment='推广员关联时间')
    user_type = Column(String(32), nullable=False, server_default=text("''"), comment='用户类型')
    is_promoter = Column(TINYINT(1), index=True, server_default=text("'0'"), comment='是否为推广员')
    pay_count = Column(INTEGER(10), server_default=text("'0'"), comment='用户购买次数')
    spread_count = Column(INTEGER(11), server_default=text("'0'"), comment='下级人数')
    addres = Column(String(255), server_default=text("''"), comment='详细地址')
    adminid = Column(INTEGER(10), server_default=text("'0'"), comment='管理员编号 ')
    login_type = Column(String(36), nullable=False, server_default=text("''"), comment='用户登陆类型，h5,wechat,routine')
    last_login_time = Column(TIMESTAMP, comment='最后一次登录时间')
    clean_time = Column(TIMESTAMP, comment='清除时间')
    path = Column(String(255), nullable=False, server_default=text("'/0/'"), comment='推广等级记录')
    subscribe = Column(TINYINT(4), server_default=text("'0'"), comment='是否关注公众号')
    roles = Column(String(255), comment='后台管理员权限')
    subscribe_time = Column(TIMESTAMP, comment='关注公众号时间')
    sex = Column(TINYINT(1), server_default=text("'1'"), comment='性别，0未知，1男，2女，3保密')
    country = Column(String(20), server_default=text("'CN'"), comment='国家，中国CN，其他OTHER')
    promoter_time = Column(TIMESTAMP, comment='成为分销员时间')
    del_flag = Column(TINYINT(1), index=True, server_default=text("'0'"), comment='删除标志（0正常 1删除）')
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')



