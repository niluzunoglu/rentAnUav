# Generated by Django 4.1.7 on 2023-02-21 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uav',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='uav',
            name='flightHours',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='uav',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
