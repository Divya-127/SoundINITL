# Generated by Django 3.2.4 on 2021-11-11 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.user'),
        ),
    ]
