# Generated by Django 3.2.4 on 2021-11-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0015_rename_user_id_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='user',
        ),
        migrations.AddField(
            model_name='song',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
