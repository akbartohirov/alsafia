# Generated by Django 3.2.12 on 2022-07-06 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220705_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_uuid',
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Faqat o'zbek raqamlarigina tasdiqlanadi", regex='^998[0-9]{2}[0-9]{7}$')], verbose_name='Telefon raqam'),
        ),
    ]
