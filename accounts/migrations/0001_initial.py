# Generated by Django 3.0.3 on 2020-02-17 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone_number', models.IntegerField(max_length=11, verbose_name='National Phone Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]