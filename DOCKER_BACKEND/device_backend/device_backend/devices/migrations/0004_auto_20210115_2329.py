# Generated by Django 3.0.11 on 2021-01-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20210114_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='keep_alive',
            field=models.DateTimeField(),
        ),
    ]
