# Generated by Django 4.2.7 on 2023-12-04 09:01

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pic',
            field=models.ImageField(blank=True, default='static/img/grid/grid_1.png', null=True, upload_to=home.models.unique_name),
        ),
    ]
