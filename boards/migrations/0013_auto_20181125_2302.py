# Generated by Django 2.1.2 on 2018-11-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0012_auto_20181125_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='last_off_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='last_on_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]