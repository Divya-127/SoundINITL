# Generated by Django 3.2.4 on 2021-11-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_alter_song_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
