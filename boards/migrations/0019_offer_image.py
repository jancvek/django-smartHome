# Generated by Django 2.1.2 on 2018-12-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0018_farm_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
