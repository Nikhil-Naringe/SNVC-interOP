# Generated by Django 4.0.3 on 2024-02-28 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_testsuitename_test_suite'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsuitename',
            name='ip_address',
            field=models.GenericIPAddressField(default=1, verbose_name='IP Address'),
            preserve_default=False,
        ),
    ]
