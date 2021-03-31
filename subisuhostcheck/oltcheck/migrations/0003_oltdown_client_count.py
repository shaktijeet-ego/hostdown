# Generated by Django 3.1.7 on 2021-03-30 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oltcheck', '0002_olt_client_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='oltdown',
            name='client_count',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oltcheck.olt'),
            preserve_default=False,
        ),
    ]
