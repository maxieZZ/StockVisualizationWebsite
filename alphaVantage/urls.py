"""alphaVantage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path as url # changed from re_path to path due to new version!
from django.contrib import admin
from django.urls import path
import stockVisualizer.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("", stockVisualizer.views.home), # makes sure home function in views.py is called when user visits homepage in web browser
    path('get_stock_data/', stockVisualizer.views.get_stock_data), # makes sure get_stock_data() in views.py is called when home.html makes an AJAX POST request to /get_stock_data/ URL
]
