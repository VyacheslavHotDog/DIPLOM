# Generated by Django 4.0.1 on 2022-03-16 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_house_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='city',
        ),
    ]