# Generated by Django 3.0.6 on 2020-05-28 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_queue'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='arrival_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='datetime arrival'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='queue_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime queue'),
        ),
    ]
