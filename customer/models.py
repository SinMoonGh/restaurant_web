from typing import Any
from django.db import models
from Chinese.models import Category, Food
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _



# Create your models here.




class Cart(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)


