# Generated by Django 3.0.3 on 2020-02-19 20:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_sessioneventmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessioneventmodel',
            name='_login_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Login Time'),
        ),
    ]
