import redis
import random
import hashlib
import bcrypt

# ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALL_CHARS = '0123456789'


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()


def gen_random_code(length=4):
    return ''.join(random.choice(ALL_CHARS) for _ in range(length))





# 生成哈希密码
def generate_hash(password):
    # 生成盐值并将密码哈希
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

redis_set = redis.StrictRedis(host="192.168.0.10", port=6379)





