# Generated by Django 4.2.3 on 2023-07-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_ocrimage_fully_segmented_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
    ]
