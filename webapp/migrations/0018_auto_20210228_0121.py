# Generated by Django 3.1.4 on 2021-02-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20210228_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamregistration',
            name='id',
        ),
        migrations.AddField(
            model_name='teamregistration',
            name='team_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
