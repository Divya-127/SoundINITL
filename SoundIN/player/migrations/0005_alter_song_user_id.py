# Generated by Django 3.2.4 on 2021-11-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_auto_20211111_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='user_id',
            field=models.IntegerField(default=2),
        ),
    ]