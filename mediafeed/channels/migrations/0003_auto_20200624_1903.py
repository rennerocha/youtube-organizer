# Generated by Django 3.0.7 on 2020-06-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0002_auto_20200624_1855"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_id",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
