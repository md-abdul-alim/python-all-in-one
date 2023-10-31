from celery import shared_task
import uuid
import pandas as pd
from .models import Product
import time
from django.conf import settings

@shared_task
def handle_sleep():
    print("Handle sleep started")
    time.sleep(20)


@shared_task
def export_product_excel():
    # time.sleep(30)
    objs = Product.objects.all()

    payload = []
    for obj in objs:
        payload.append({
            'title': obj.title,
            'price': obj.price
        })

    df = pd.DataFrame(payload)
    df.to_csv(f'{uuid.uuid4()}.csv', encoding='UTF-8')

