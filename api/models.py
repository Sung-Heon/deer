from django.db import models

# Create your models here.
from django.contrib.gis.db import models


# Create your models here.

class Area(models.Model):
    boundary = models.PolygonField()
    center = models.PointField()
    coords = models.MultiPointField()

    class Meta:
        db_table = 'area'


class Deer(models.Model):
    name = models.CharField(max_length=20)
    area = models.ForeignKey("Area", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'deer'


class BasePricing(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'base_pricing'


class User(models.Model):
    name = models.CharField(max_length=20)
    base_pricing = models.ForeignKey("BasePricing", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'user'


class UserRecords(models.Model):
    deer = models.ForeignKey("Deer", on_delete=models.DO_NOTHING)
    end_lat_lng = models.PointField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'user_records'
        get_latest_by = ["end_at"]

class ParkingZone(models.Model):
    center_lat_lng = models.PointField()
    radius = models.FloatField()
    area = models.ForeignKey("Area", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'parking_zone'


class ForbiddenArea(models.Model):
    boundary = models.PolygonField()
    coords = models.MultiPointField()
    area = models.ForeignKey("Area", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'forbidden_area'
