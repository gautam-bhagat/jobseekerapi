# Generated by Django 4.1.7 on 2023-03-27 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_team_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='timestamp',
            field=models.IntegerField(max_length=100),
        ),
    ]
