# Generated by Django 5.0.6 on 2024-07-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_rename_numder_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
