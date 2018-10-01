# Generated by Django 2.1.1 on 2018-10-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iwmac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='last_read_value',
            new_name='last_value',
        ),
        migrations.AddField(
            model_name='sensor',
            name='last_timestamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
