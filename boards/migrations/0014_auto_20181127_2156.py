# Generated by Django 2.1.2 on 2018-11-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0013_auto_20181125_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='description',
            field=models.TextField(),
        ),
    ]