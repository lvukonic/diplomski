# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Patient(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=30)
	age = models.IntegerField(default=0)
	
class Measurement(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	height = models.IntegerField(default=0)
	bmi = models.DecimalField(max_digits=5, decimal_places=2)
	

# Create your models here.
