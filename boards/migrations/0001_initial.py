# Generated by Django 2.1.2 on 2018-10-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rain_prob', models.IntegerField()),
                ('clouds', models.IntegerField()),
                ('save_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
