# Generated by Django 3.1.4 on 2021-02-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20210228_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='class_cap',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='team',
            field=models.IntegerField(default=0),
        ),
    ]
