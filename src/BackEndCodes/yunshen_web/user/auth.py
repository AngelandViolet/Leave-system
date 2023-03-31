# 部门:人工智能
# 编写人:张开然
# 开发日期: 2023/03/15
# !/usr/bin/python
# -*- coding: UTF-8 -*-
import secrets
from datetime import datetime, timedelta
from typing import Optional

import jwt

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300000


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decoded_token(token: str):
    """
    返回数据为username和uid组成的字典。
    :param token: 令牌
    :return: username和uid组成的字典
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.exceptions.InvalidTokenError:
        return False
