# Generated by Django 2.1.1 on 2018-10-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.UUIDField(unique=True)),
                ('element', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=50)),
                ('eng_unit', models.CharField(max_length=20)),
                ('last_read_value', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]