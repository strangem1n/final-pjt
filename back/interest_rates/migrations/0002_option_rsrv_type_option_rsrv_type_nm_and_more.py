# Generated by Django 4.2.16 on 2025-05-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest_rates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='rsrv_type',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='option',
            name='rsrv_type_nm',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='intr_rate_type_nm',
            field=models.CharField(max_length=10),
        ),
    ]
