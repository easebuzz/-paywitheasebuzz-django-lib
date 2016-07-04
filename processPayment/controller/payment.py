__author__ = 'jaishankar'

from django.shortcuts import render, redirect
from processPayment.forms.preRequisiteForm import PayWithEasebuzzPreRequisiteForm
from django.conf import settings
from django.core.urlresolvers import reverse
from preserialize.serialize import serialize
from django.http import JsonResponse , HttpResponse
from hashlib import sha512
import requests
import json
from processPayment.lib.payment_lib import *

def index(request):
    if request.method == 'GET':
        preForm = PayWithEasebuzzPreRequisiteForm()
        return render(request,'preRequisite.html',{"preRequisiteForm":preForm})
    if request.method == 'POST':
        preForm = PayWithEasebuzzPreRequisiteForm(request.POST)
        print preForm
        if not preForm.is_valid():
            print "not validddd"
            print "Errors: %s"  %preForm.non_field_errors()
            return render(request,'preRequisite.html',{"preRequisiteForm":preForm})
        else:
            return proceedToPayment(request,'test1234')




def proceedToPayment(request,txnId):
    uname = request.POST['payer'].strip()
    amount = request.POST['amount'].strip()
    uemail = request.POST['email'].strip()
    uphone = request.POST['phone'].strip()
    KEYS = [settings.MERCHANT_KEY,txnId, amount, 'anyText', uname, uemail,'', '', '', '', '','', '', '', '', '']
    hash=generate_hash(KEYS)
    print hash
    item = {
                "key": settings.MERCHANT_KEY,
                "txnid": txnId,
                "amount": amount,
                "productinfo": "anyText",
                "firstname": uname,
                "phone": uphone,
                "email": uemail,
                "surl": request.build_absolute_uri(reverse('epSuccessPayment')),
                "furl": request.build_absolute_uri(reverse('epFailPayment')),
                "hash": hash,
                "udf1": "",
                "udf2": "",
                "udf3": "",
                "udf4": "",
                "udf5": ""
                }
    resp = get_redirect_url(item)
    r = serialize(resp.content)
    print r;
    r = json.loads(r)
    print r
    print resp
    if r['status'] == 0:
       return JsonResponse({'status':'201','error':r['data']})
    elif r['status'] == 1:
       link_id = r['data']
       url = settings.URL_PAY+link_id
       print url
       return HttpResponse("""
                        <html>
                        <head><title>Redirecting...</title></head>
                        <body>
                        <form action='%s' method='post' name="paywitheasebuzz">
                            redirecting to pay.easebuzz.in ....
                        </form>
                        </body>
                        <script language='javascript'>
                            window.onload = function(){
                            document.forms['paywitheasebuzz'].submit()
                            }
                        </script>
                        </html>
                    """ % url)
    else:
       return JsonResponse({'status':'202','error':'Due To security concerns we reject this transaction'})

    print "done";


def epSuccessPayment(request):
    KEYS = [settings.MERCHANT_KEY, request.POST['txnid'], request.POST['amount'],request.POST['productinfo'], request.POST['firstname'], request.POST['email'],'', '', '', '', '','', '', '', '', '']
    status = request.POST['status']
    result={}
    if verify_hash(KEYS, status) == request.POST['hash']:
        return JsonResponse({'status':'200','success':serialize(request)})
    else :
        return JsonResponse({'status':'404','error':serialize(request)})

def epFailPayment(request):
    KEYS = [settings.MERCHANT_KEY, request.POST['txnid'], request.POST['amount'],request.POST['productinfo'], request.POST['firstname'], request.POST['email'],'', '', '', '', '','', '', '', '', '']
    status = request.POST['status']
    print "%%%%%%%%%%%%%%%%%%%%%"
    print "%%%%%%%%%%%%%%%%%%%%%"
    if verify_hash(KEYS, status) == request.POST['hash']:
        return  JsonResponse({'status':'false','cancelreason':serialize(request)})
    else:
       return JsonResponse({'status':'false','reason':'unethical activity detected, transaction stands cancelled'})


