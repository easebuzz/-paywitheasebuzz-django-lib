__author__ = 'jaishankar'


from hashlib import sha512
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
import random, string


KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'phone', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5')

# KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
#         'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
#         'udf9',  'udf10')
def generate_hash(data):
    hashstring=""
    for key in data:
        hashstring=hashstring+str(key)+"|"
    hashstring=hashstring+settings.SALT
    return sha512(hashstring).hexdigest().lower()

def get_redirect_url(item):
    a= requests.post(settings.URL_GETLINK,data=item)
    return a

def verify_hash(data, status):
    hashstring = ""
    hashstring = hashstring+settings.SALT+"|"+status+"|"
    for key in reversed(data):
        hashstring = hashstring+str(key)+"|"
    hashstring = hashstring[:-1]
    return sha512(hashstring).hexdigest().lower()

def send_redirect(link_id):
    return HttpResponse("""
                            <html>
                            <head><title>Redirecting...</title></head>
                            <body>
                            <form action='%s' method='post' name="paywitheasebuzz">
                            </form>
                            </body>
                            <script language='javascript'>
                                window.onload = function(){
                                document.forms['paywitheasebuzz'].submit()
                                }
                            </script>
                            </html>
                        """ % (settings.URL_PAY+link_id)
                        )

def randomString(length):
   return ''.join(random.choice(string.uppercase+'1234567890') for i in range(length))