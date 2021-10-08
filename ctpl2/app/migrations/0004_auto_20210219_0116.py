# Generated by Django 3.1.5 on 2021-02-18 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210219_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boq',
            old_name='Company_Name',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='boq',
            old_name='OEM_Name',
            new_name='OEM',
        ),
        migrations.RenameField(
            model_name='boq',
            old_name='Project_Name',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='cop',
            old_name='OEM_Name',
            new_name='OEM',
        ),
        migrations.RenameField(
            model_name='cop',
            old_name='Project_Name',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='dc',
            old_name='Company_Name',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='dc',
            old_name='OEM_Name',
            new_name='OEM',
        ),
        migrations.RenameField(
            model_name='dc',
            old_name='Project_Name',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='ir',
            old_name='Company_Name',
            new_name='Company',
        ),
        migrations.RenameField(
            model_name='ir',
            old_name='OEM_Name',
            new_name='OEM',
        ),
        migrations.RenameField(
            model_name='ir',
            old_name='Project_Name',
            new_name='Project',
        ),
    ]