# Generated by Django 3.1.4 on 2021-02-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210220_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='council',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='event',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='paid',
        ),
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.CharField(default="{% static 'webapp/assets/images/profile.svg' %}", max_length=100),
        ),
    ]
