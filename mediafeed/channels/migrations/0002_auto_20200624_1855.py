# Generated by Django 3.0.7 on 2020-06-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("channels", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video", name="video_id", field=models.CharField(max_length=20),
        ),
    ]