# Generated by Django 4.2.3 on 2023-07-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_remove_ocrimage_fully_segmented_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocrimage',
            name='fully_segmented_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/fully_segmented_images/'),
        ),
    ]
