# Generated by Django 2.1.2 on 2018-12-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0014_auto_20181127_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='measure_place',
            field=models.CharField(choices=[('smasa', 'Soba Maša'), ('sspal', 'Soba spalnica'), ('kopal', 'Kopalnica'), ('kuhin', 'Kuhinja'), ('balkz', 'Balkon zahod'), ('zdnev', 'Dnevna zgoraj')], max_length=5),
        ),
        migrations.AlterField(
            model_name='housedata',
            name='measure_place',
            field=models.CharField(choices=[('smasa', 'Soba Maša'), ('sspal', 'Soba spalnica'), ('kopal', 'Kopalnica'), ('kuhin', 'Kuhinja'), ('balkz', 'Balkon zahod'), ('zdnev', 'Dnevna zgoraj')], max_length=5),
        ),
    ]
