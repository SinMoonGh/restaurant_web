from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(verbose_name='카테고리', max_length=100, default='')

# Create your models here.
class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    name = models.CharField(verbose_name='음식 이름', max_length=100, default='')
    description = models.CharField(verbose_name='음식 설명', max_length=500, default='')
    price = models.IntegerField(verbose_name='음식 가격', default=0)
    image_url = models.URLField(blank=True, null=True)
    def get_image_path(instance, filename):
        return f'{settings.MEDIA_ROOT}/images/{filename}'

    image = models.ImageField(upload_to=get_image_path)


# class User(models.Manager):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
#     user_name = models.CharField(verbose_name='이름', max_length=20)
#     user_phone = models.CharField(verbose_name='전화번호', max_length=20)



