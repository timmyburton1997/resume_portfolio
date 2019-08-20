# Generated by Django 2.2.4 on 2019-08-18 19:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('volunteering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteering',
            name='time',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteering',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
    ]
