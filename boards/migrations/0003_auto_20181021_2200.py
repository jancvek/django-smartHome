# Generated by Django 2.1.2 on 2018-10-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20181021_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinedata',
            name='humidity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='onlinedata',
            name='measure_place',
            field=models.CharField(choices=[('KRA', 'Kranj'), ('NAK', 'Naklo'), ('TRZ', 'Tržič'), ('LLE', 'Letališče Lesce')], default='TRZ', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onlinedata',
            name='temp',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
