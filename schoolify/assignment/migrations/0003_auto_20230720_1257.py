# Generated by Django 3.2.20 on 2023-07-20 09:57

from django.db import migrations, models
import schoolify.auth_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_alter_assignmentcooking_dish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentcooking',
            name='assignment_name',
            field=models.TextField(help_text='Please fill in the name of your assignment as per homework.', verbose_name='Name of assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentcooking',
            name='dish_image',
            field=models.ImageField(blank=True, help_text='Please upload a picture of your dish.', null=True, upload_to='', validators=[schoolify.auth_app.validators.image_size_validator_10mb]),
        ),
        migrations.AlterField(
            model_name='assignmentcooking',
            name='ingredients',
            field=models.TextField(help_text='Please fill in the ingredients of your dish.'),
        ),
        migrations.AlterField(
            model_name='assignmentcooking',
            name='preparation_time',
            field=models.TimeField(help_text='Please fill in the full reparation time, together with cooking time.'),
        ),
        migrations.AlterField(
            model_name='assignmentcooking',
            name='recipe_name',
            field=models.TextField(help_text='Please enter the name of your recipe.'),
        ),
        migrations.AlterField(
            model_name='assignmentenglish',
            name='assignment_name',
            field=models.TextField(help_text='Please fill in the name of your assignment as per homework.', verbose_name='Name of assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentenglish',
            name='essay',
            field=models.TextField(help_text='Please write your essay here.'),
        ),
        migrations.AlterField(
            model_name='assignmentenglish',
            name='external_resources_used',
            field=models.URLField(blank=True, help_text='Please write the URL of the external resource used.', null=True),
        ),
        migrations.AlterField(
            model_name='assignmentmathematics',
            name='assignment_name',
            field=models.TextField(help_text='Please fill in the name of your assignment as per homework.', verbose_name='Name of assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentmathematics',
            name='solution',
            field=models.TextField(help_text='Please write the solution here'),
        ),
        migrations.AlterField(
            model_name='assignmentmusic',
            name='assignment_name',
            field=models.TextField(help_text='Please fill in the name of your assignment as per homework.', verbose_name='Name of assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentmusic',
            name='song',
            field=models.FileField(help_text='Please upload a record of your song here', upload_to=''),
        ),
    ]
