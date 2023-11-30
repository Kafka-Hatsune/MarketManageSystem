from rest_framework import serializers


class NewsImgUploadSerializer(serializers.Serializer):

    img = serializers.ImageField(
        label="图片",
        max_length=256,   # 图片名最大长度
        use_url=True,     # 设为True则URL字符串值将用于输出表示,设为False则文件名字符串值将用于输出表示
        error_messages={
            'invalid': '图片参数错误'
        }
    )
