# Generated by Django 2.1.2 on 2018-12-27 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0022_auto_20181226_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='farm',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='boards.Farm'),
            preserve_default=False,
        ),
    ]
