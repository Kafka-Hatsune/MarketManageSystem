import os
from datetime import datetime

import jwt
from django.views.static import serve
from rest_framework.request import Request

from backend import settings

SECRET_KEY = 'awsfdf'


def gen_token(name: str):
    dict = {
        'username': name
    }
    token = jwt.encode(dict, SECRET_KEY, algorithm='HS256')
    return token


def get_header_token(req: Request):
    if req.headers.get('Authorization'):
        #vprint(req.headers['token'])
        return req.headers['Authorization'][7:]


def decode_token(token):
    try:
        dict = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception:
        return None
    return dict


def serve_media(request, path):
    return serve(request, path, document_root=settings.MEDIA_ROOT)


def image_upload_path(instance, filename):
    # 获取当前日期和时间
    current_time = datetime.now()
    # 获取文件的扩展名
    ext = os.path.splitext(filename)[1]
    # 构造新的文件名，例如：image_20211124_120000.png
    new_filename = f"image_{current_time.strftime('%Y%m%d_%H%M%S')}{ext}"
    # 返回文件的存储路径
    return os.path.join('images', new_filename)
