# Generated by Django 4.0.3 on 2024-02-15 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_remove_testsuite_mapping_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuitename',
            name='test_suite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.testsuite'),
        ),
    ]