# Generated by Django 2.2.4 on 2019-08-18 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190813_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='send',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
