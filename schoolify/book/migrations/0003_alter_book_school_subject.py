# Generated by Django 3.2.20 on 2023-07-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='school_subject',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('English', 'English'), ('Music', 'Music'), ('Cooking', 'Cooking')], max_length=11),
        ),
    ]
