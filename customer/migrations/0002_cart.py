# Generated by Django 5.0.3 on 2024-04-16 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chinese', '0002_food_image_url'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Chinese.food')),
            ],
        ),
    ]
