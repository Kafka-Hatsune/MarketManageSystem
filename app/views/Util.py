from app.models import Product, Comment, ProductImages


def getProductData(p: Product):
    data = {
        'typeName': p.product_type.type,
        'productId': p.id,
        'productName': p.product_name,
        'price': p.price,
        'description': p.description,
        'sale': p.sale,
        'stock': p.stock,
        'createdTime': p.get_create_time(),
        'productPic': [pi.img.get_url() for pi in ProductImages.objects.filter(product=p)],
        'comments': [{
            'id': c.id,
            'text': c.text,
            'createdTime': c.get_create_time(),
            'publisher': {
                # 'id': c.publisher.id,
                'userName': c.publisher.name,
                'avatar': None if not p.publisher.avatar else p.publisher.avatar.get_url()
            },
        } for c in Comment.objects.filter(item=p)],
    }
    return data

