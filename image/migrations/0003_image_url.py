# Generated by Django 5.1.3 on 2024-11-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_remove_image_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.TextField(default=0, unique=True),
            preserve_default=False,
        ),
    ]