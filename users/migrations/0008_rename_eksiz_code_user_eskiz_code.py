# Generated by Django 3.2.12 on 2022-07-06 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='eksiz_code',
            new_name='eskiz_code',
        ),
    ]
