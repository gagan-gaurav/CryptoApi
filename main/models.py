from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Crypto(models.Model):
	id = models.PositiveIntegerField(primary_key = True, unique = True, null = False, default = 0)
	cmc_rank = models.PositiveIntegerField(unique = True, null = True, default = 0)
	name = models.CharField(max_length = 50)
	symbol = models.CharField(max_length = 30)
	curculatingSupply = models.DecimalField(max_digits = 18, decimal_places = 2)
	priceInUSD = models.DecimalField(max_digits = 18, decimal_places = 2)
	timeStamp = models.DateTimeField()
