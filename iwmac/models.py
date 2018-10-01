from django.db import models


class Sensor(models.Model):
    oid = models.UUIDField(unique=True)
    element = models.CharField(max_length=200)
    name = models.CharField(max_length=100, null=False)
    unit = models.CharField(max_length=50)
    eng_unit = models.CharField(max_length=20)
    last_timestamp = models.BigIntegerField(default=0)
    last_value = models.DecimalField(decimal_places=2, max_digits=9)
