# Generated by Django 4.1 on 2023-04-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0005_photography_date_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photography",
            name="picture",
            field=models.ImageField(blank=True, upload_to="pictures/%Y/%m/%d/"),
        ),
    ]
