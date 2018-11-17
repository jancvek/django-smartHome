# Generated by Django 2.1.2 on 2018-10-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20181027_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_ident', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('measure_place', models.CharField(choices=[('smasa', 'Soba Maša'), ('sspal', 'Soba spalnica'), ('kopal', 'Kopalnica'), ('kuhin', 'Kuhinja'), ('balkz', 'Balkon zahod')], max_length=5)),
                ('rssi', models.IntegerField(null=True)),
            ],
        ),
    ]