# Generated by Django 3.2.20 on 2023-08-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_auto_20230801_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentmathematics',
            name='solution',
            field=models.TextField(help_text='Please write the solution here', max_length=1000),
        ),
    ]
