# Generated by Django 5.0.7 on 2024-07-27 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_bookreview_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
