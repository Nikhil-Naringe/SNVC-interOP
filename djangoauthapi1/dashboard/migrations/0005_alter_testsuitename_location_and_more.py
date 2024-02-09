# Generated by Django 4.0.3 on 2024-02-07 09:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_testsuitename_name_testsuitename_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuitename',
            name='location',
            field=models.FileField(help_text='Enter folder location', upload_to='test_locations/'),
        ),
        migrations.AlterField(
            model_name='testsuitename',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Invalid password format', regex='^[\\w.@+-]+$')]),
        ),
        migrations.AlterField(
            model_name='testsuitename',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]