# Generated by Django 3.2 on 2021-05-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_delete_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='media_gallery',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
