from django.db import models


class Burger_king(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(max_length=255)
    lng = models.FloatField(max_length=255)
    address = models.CharField(max_length=255)


class Mcdonalds(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(max_length=255)
    lng = models.FloatField(max_length=255)
    address = models.CharField(max_length=255)


class Kfc(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField(max_length=255)
    lng = models.FloatField(max_length=255)
    address = models.CharField(max_length=255)