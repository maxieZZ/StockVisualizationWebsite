# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Define Django database model called StockData...

class StockData(models.Model):
    symbol = models.TextField(null=True) # stores ticker string of stock
    data = models.TextField(null=True) # stores historical prices and moving average values for a given ticker