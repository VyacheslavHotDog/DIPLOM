# Generated by Django 4.0.1 on 2022-03-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
