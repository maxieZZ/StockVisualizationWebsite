# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockData

import requests
import json
from .SecretAPI import APIKEY_PHRASE


APIKEY = APIKEY_PHRASE
# NOTE: replace 'my_alphav_api_key' with actual Alpha Vantage API key obtained from https://www.alphavantage.co/support/#api-key


DATABASE_ACCESS = True 
# if False, app will always query Alpha Vantage APIs regardless of whether stock data for a given ticker is already in local database


# standard way for Django backend to render an HTML file (in this case home.html)...
def home(request):
    return render(request, 'home.html', {})

def is_ajax(request): # added this because built in function was depreciated!
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# get_stock_data() takes an AJAX POST request from home.html file and returns a JSON dictionary of stock data back to AJAX loop...
@csrf_exempt
def get_stock_data(request):
    if is_ajax(request): # check if request is AJAX POST from frontend
        ticker = request.POST.get('ticker', 'null') # get ticker from AJAX POST request
        ticker = ticker.upper()

        if DATABASE_ACCESS == True:
            # checking if database already has data stored for this ticker before querying the Alpha Vantage API
            if StockData.objects.filter(symbol=ticker).exists(): 
                # data is already in database so get data from database directly and send it back to frontend AJAX call
                print("Ticker has already been saved in DB, fetching data now...")
                entry = StockData.objects.filter(symbol=ticker)[0] # Djangos way of saying SELECT * FROM StockData WHERE symbol = ticker
                #print(entry.data)
                return HttpResponse(entry.data, content_type='application/json')

        # obtain stock data from Alpha Vantage APIs
        # get adjusted close data
        # queries Alpha Vantage's Daily Adjusted API and parses data into a JSON dictionary through the .json() routine...
        print("Ticker is not found, querrying Alpha Vantage's Daily Adjusted API")
        price= requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={APIKEY}').json() # get the quote (ie current price) data
        
        # get SMA (simple moving average) data
        sma_series = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=daily&time_period=10&series_type=close&apikey={APIKEY}').json()

        # packages up the adjusted close JSON data and the simple moving average JSON data into a single dictionary output_dictionary (labeled by quote and sma to distinguish)...
        output_dictionary = {}
        output_dictionary['quote'] = price
        output_dictionary['sma'] = sma_series

        # save stock data to database (so that data can be recycled from database next time without querying Alpha Vantage APIs again)
        #print(json.dumps(output_dictionary))
        temp = StockData(symbol=ticker, data=json.dumps(output_dictionary))
        temp.save()

        # return data back to frontend AJAX POST loop for charting
        return HttpResponse(json.dumps(output_dictionary), content_type='application/json')

    else:
        message = "Not Ajax"
        return HttpResponse(message)
