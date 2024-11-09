from fastapi import APIRouter,Body
from typing import Dict
from sqlalchemy import desc
from app.db.dataBase import Session
from app.db.model.EbUser import EbUser
from app.db.model.EbUser import Session as EbSession
from app.util.TokenUtil import get_user_id
from app.util.TokenUtil import Jwt_Token
from app.util.dataModel import Login_Data
from app.db.model.UserPointsTable import UserPointsTable
from app.util.conf import redis_set
from app.util.conf import gen_random_code
from app.util.conf import generate_hash
from app.util.sms import Sample
import secrets
import bcrypt



router = APIRouter(tags=["登录"])




@router.post("/login",summary='login')
async def login(item: Login_Data):
    eb_session = EbSession()
    result = {'status': 200}  # 初始化结果字典，设置初始状态为 200 表示成功
    local_session = Session()
    phone = item.phone
    code = item.code
    password = item.password
    try:
        if password:
            # 如果提供了密码
            user = eb_session.query(EbUser).filter_by(user_name=phone).first()  # 查询用户是否存在
            password = password.encode()  # 密码转义
            secret_key = secrets.token_urlsafe(16)
            if user and bcrypt.checkpw(password,user.password.encode()):  # 判断密码和用户
                # 如果用户存在且密码正确
                # old_token = redis_set.getset(phone, secret_key)
                token = Jwt_Token(user.user_id, str(phone))

                cred_data = local_session.query(UserPointsTable.remainingDuration).filter(UserPointsTable.userId==user.user_id).first()
                # print(cred_data)
                cred = cred_data[0] if cred_data else 0
                nickname = user.nickname
                avatar = user.avatar
                user_type = user.user_type
                avaters='http://47.115.205.23:5007//'+avatar

                print(avaters)
                phone = user.phone


                return {"access_token_key":secret_key,
                                   "user_data":{'nickname': nickname, "avatar": avaters, 'phone': phone,
                                              "integral": cred, "user_type": user_type, 'newtoken': token},
                                   "message":"密码登陆成功", "status":200}  # 返回成功消息和访问令牌

            else:
                # 用户不存在或密码不匹配
                result['status'] = 401  # 设置状态为 401 表示未授权
                result["message"] = "无效的手机号或密码"  # 返回消息表示无效的手机号或密码
                return result  # 返回结果字典作为 JSON 响应

        elif code:
            # 如果提供了验证码
            user = eb_session.query(EbUser).filter_by(user_name=phone).first()  # 查询用户是否存在
            stored_code = redis_set.get(f"lsms_code{phone}")  # 获取存储的验证码
            print(stored_code)
            secret_key = secrets.token_urlsafe(16)
            if stored_code:
                stored_code = stored_code.decode()  # 解码存储的验证码
                print(code,stored_code)
                if code == stored_code:
                    token = Jwt_Token(user.user_id, str(phone))

                    # local_session = localSession()

                    cred_data = local_session.query(UserPointsTable.remainingDuration).filter(
                        UserPointsTable.userId == user.user_id).first()

                    cred = cred_data[0] if cred_data else 0
                    nickname = user.nickname
                    avatar = user.avatar
                    user_type = user.user_type
                    avaters = 'http://47.115.205.23:5007//' + avatar

                    print(avaters)
                    phone = user.user_name

                    return {"access_token_key":secret_key,
                                   "user_data":{'nickname': nickname, "avatar": avaters, 'phone': phone,
                                              "integral": cred, "user_type": user_type, 'newtoken': token},
                                   "message":"驗證碼登陸成功", "status":200}  # 返回成功消息和访问令牌
                else:
                    result['status'] = 402  # 设置状态为 402 表示验证失败
                    result["message"] = "验证码错误"  # 返回消息表示验证码错误
            else:
                result['status'] = 401  # 设置状态为 401 表示未授权
                result["message"] = "验证码不存在"  # 返回消息表示验证码不存在

            return result  # 返回结果字典作为 JSON 响应


    except Exception as e:
        print(e)
        return {'message': 'error', 'status': 10000}



@router.post("/sms",summary='sms')
async def sms(phone: str):
    session = EbSession()
    chatsession = Session()
    try:
        user = session.query(EbUser).filter_by(user_name=phone).first()  # 检查用户是否已注册
        if user is not None:
            new_code = gen_random_code()
            print(new_code)
            redis_set.set(phone, "True", 57)
            redis_set.set(f"lsms_code{phone}", new_code, 3000)
            Sample.main([str(phone), str(new_code)])
            return {"status": 200, "msg": "验证码获取成功", "code": new_code}
        else:
            password = generate_hash(phone[-6:])
            user_add = EbUser(user_name=phone, password=password, nickname=f'{phone}', avatar='crmebimage/public/maintain/2023/02/23/1c0fa967eb764d918f064744cc51dc70a6f2bj3sha.jpg')
            session.add(user_add)
            session.commit()
            userid = user_add.user_id
            print(userid,type(userid))
            points_add = UserPointsTable(userId=userid, totalDuration=15, remainingDuration=15, isDeleted=0)
            chatsession.add(points_add)
            chatsession.commit()
            print(points_add.id)
            print()
            if redis_set.get(phone) is None:
                redis_set.set(phone, "True", 57)
                new_code = gen_random_code()
                redis_set.set(f"lsms_code{phone}", new_code, 3000)
                print(new_code)
                Sample.main([str(phone), str(new_code)])
                return {"status": 200, "msg": "验证码获取成功", "code": new_code}
            return {"status": 401, "msg": "频繁获取"}
    except Exception as e:

        return {"status": 500, "msg": str(e)}
    finally:
        session.close()


