# StockVisualizationWebsite

Interactive stock visualization website with Python/Django &amp; Alpha Vantage APIs utilizing AJAX, server-side scripting, and database models

Inspired by the following tutorial: https://www.alphavantage.co/stock-price-tracker-website-python-django/

Project Keywords: web development, data visualization, HTML, Javascript/AJAX, server-side scripting, SQL, Python/Django

An image of the final working homepage is shown in the screenshot below. Note that the default displays the current price of the FBTC ticker along with the SMA data from the past 500 trading days.

<img src="images/home_page.png?raw=true"/>

To view an alternative ticker, the user can type the desired ticker of their choice into the search bar and select "submit" in order to display the current price and SMA data for that given ticker. An example of this is shown in the image below where the user has typed the ticker symbol for Apple (AAPL).

<img src="images/search_result.png?raw=true"/>

If the user types an incorrect ticker symbol or a ticker that does not exist in the alphaVantage database, a pop up alert will prompt the user to enter a different ticker as shown in the screenshot below. 

<img src="images/error_msg.png?raw=true"/>

SUMMARY OF FUNCTIONALITIES: 
1. Page should display current price and simple moving average (SMA) the defualt ticker (FBTC) covering most recent 500 trading days
2. When user enters new ticker in textbox and hits "submit," existing chart should be replaced with the current price and SMA data of new ticker
3. When a user enters a ticker that does not exist, an alert window should pop up to notify the user of their error and prompt them to retry

STEPS INVOLVED:
1. Install dependencies and set up project
2. Create database model (models.py)
3. Create frontend UI (home.html)
4. Create backend logic (views.py)
5. Set up Django URL routing (urls.py)
6. Run the web application locally (using http://localhost:8000/)

TO RUN: 
>> source python_env/bin/activate
>> python3 manage.py runserver

