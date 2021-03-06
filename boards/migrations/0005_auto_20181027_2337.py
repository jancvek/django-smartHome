# Generated by Django 2.1.2 on 2018-10-27 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_housedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='housedata',
            name='humidity',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='housedata',
            name='measure_place',
            field=models.CharField(choices=[('smasa', 'Soba Maša'), ('sspal', 'Soba spalnica'), ('kopal', 'Kopalnica'), ('kuhin', 'Kuhinja'), ('balkz', 'Balkon zahod')], default='kuhin', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='housedata',
            name='save_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='housedata',
            name='temp',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
