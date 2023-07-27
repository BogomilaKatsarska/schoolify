# Generated by Django 3.2.20 on 2023-07-21 17:58

from django.db import migrations, models
import schoolify.auth_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_profile_school_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='personal_number',
            field=models.PositiveIntegerField(unique=True, validators=[schoolify.auth_app.validators.validate_len_personal_number]),
        ),
    ]
