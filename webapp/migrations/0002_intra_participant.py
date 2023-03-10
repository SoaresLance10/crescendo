# Generated by Django 3.1.4 on 2021-03-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intra_participant',
            fields=[
                ('paticipants_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('class_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('groups', models.CharField(default='participant', max_length=100)),
            ],
        ),
    ]
