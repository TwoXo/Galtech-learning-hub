# Generated by Django 4.2.7 on 2023-12-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_video_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
