"""payWithEasebuzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from processPayment.controller import  payment
from django.contrib import admin

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^/', payment.index, name='PWE_Form'),
    url(r'^PWE_Form/?$',payment.index, name='PWE_Form'),
    url(r'^initiatePayment/?$',payment.proceedToPayment, name='initiatePayment'),
    url(r'^epSuccessPayment/?$',csrf_exempt(payment.epSuccessPayment), name='epSuccessPayment'),
    url(r'^epFailPayment/?$',csrf_exempt(payment.epFailPayment), name='epFailPayment'),



]
