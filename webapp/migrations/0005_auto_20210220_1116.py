# Generated by Django 3.1.4 on 2021-02-20 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210220_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='council_id',
            new_name='council_name',
        ),
    ]
