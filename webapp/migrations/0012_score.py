# Generated by Django 3.1.4 on 2021-02-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20210225_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
