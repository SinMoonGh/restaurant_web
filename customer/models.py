from django.db import models
from Chinese.models import Category, Food


# Create your models here.
class User(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(verbose_name='이름', max_length=20)
    user_phone = models.CharField(verbose_name='전화번호', max_length=20)


class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)


