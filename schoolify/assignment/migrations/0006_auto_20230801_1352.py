# Generated by Django 3.2.20 on 2023-08-01 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0005_auto_20230726_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentcooking',
            name='created_by',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentenglish',
            name='created_by',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentmathematics',
            name='created_by',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentmusic',
            name='created_by',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
