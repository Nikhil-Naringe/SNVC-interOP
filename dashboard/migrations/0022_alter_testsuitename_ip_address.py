# Generated by Django 4.0.3 on 2024-02-28 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_alter_testsuitename_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuitename',
            name='ip_address',
            field=models.GenericIPAddressField(verbose_name='IP Address'),
        ),
    ]