from django.http import HttpResponse

from django.shortcuts import render, redirect

import json

''' Access Easebuzz class functionalities for payment gateway

    import Easebuzz class from the easebuzz-lib/easebuzz_payment_gateway.py file

    example : from projectname.sub_folder1.file_name import class_name or function_name.
'''
from easebuzz_lib.easebuzz_payment_gateway import Easebuzz

# Based on API call change the Merchant key and salt key for (initaite payment) on testing
MERCHANT_KEY = "XXXXXXXXXX"
SALT = "XXXXXXXXXX"
ENV = "test"

# create Easebuzz object and send data
easebuzzObj = Easebuzz(MERCHANT_KEY, SALT, ENV)

def index(request):
    return render(request, 'index.html')


'''
*
* Create object for call easepay payment gate API and Pass required data into constructor.
* Get API response.
*
* param  string MERCHANT_KEY - holds the merchant key.
* param  string SALT - holds the merchant salt key.
* param  string ENV - holds the env(enviroment).
* param  string request - holds the form data.
*
* ##Return values
*
* - return array ApiResponse['status']== 1 successful.
* - return array ApiResponse['status']== 0 error.
*
* @param  string MERCHANT_KEY - holds the merchant key.
* @param  string SALT - holds the merchant salt key.
* @param  string ENV - holds the env(enviroment).
* @param  string request - holds the form data.
*
* @return array ApiResponse['status']== 1 successful.
* @return array ApiResponse['status']== 0 error.
*
'''
def initiate_payment(request):
    '''
    * Very Important Notes
    *
    * Post Data should be below formate.

        <QueryDict: {u'city': [u'aaaa'], u'zipcode': [u'123123'], u'address2': [u'aaaa'], 
        firstname': [u'jitendra'], u'state': [u'aaaa'], u'address1': [u'aaaa'], 
        u'surl': [u'http://localhost:8000/response/'], u'udf3': [u'aaaa'], 
        u'txnid': [u'T3SAT0B5OL'], u'productinfo': [u'Apple Mobile'], 
        u'furl': [u'http://localhost:8000/response/'], u'udf1': [u'aaaa'], 
        u'phone': [u'1231231235'], u'amount': [u'1.03'], u'udf2': [u'aa'], 
        u'udf5': [u'aaaa'], u'udf4': [u'aaaa'], u'country': [u'aaaa'], 
        u'csrfmiddlewaretoken': [u'6zKwuxucnwd3J2CXcFR3lj0nW8eiL8Y0i63YV3F8zvXDE4PfhjGD9WXBv72EEYZZ'], 
        u'email': [u'jitendra@gmail.com']}>
    '''
    if request.method == 'POST':

        final_response = easebuzzObj.initiatePaymentAPI(request.POST)
        result = json.loads(final_response)

        if result['status'] == 1:
            return redirect(result['data'])
        else:
            # return HttpResponse(final_response)
            return render(request, 'response.html', {'response_data': final_response})
    else:
        return render(request, 'initiate_payment.html')


'''
* Use transaction API
'''
def transaction(request):
    '''
    * Very Important Notes
    *
    * Post Data should be below formate.

        <QueryDict: {u'phone': [u'1231231235'], 
        u'csrfmiddlewaretoken': [u'X1vgdvX5eJfDeQSUx12XMuPxYmBTExTq9yOIE181qIZd9S5cCFRxA7MLxlpfxnUp'], 
        u'txnid': [u'T300'], u'amount': [u'1.03'], u'email': [u'jitendra@gmail.com']}>
    '''
    if request.method == 'POST':

        final_response = easebuzzObj.transactionAPI(request.POST)
        # return HttpResponse(final_response)
        return render(request, 'response.html', {'response_data': final_response})
    else:
        return render(request, 'transaction.html')


'''
* Use transaction date API
'''
def transaction_date(request):
    '''
    * Very Important Notes
    *
    * Post Data should be below formate.

        <QueryDict: {u'csrfmiddlewaretoken': [u'aQArNZMurJD9bPrWYRmZohRCPzsyXznnmnTTevXqDInJ6REe3vbzcUOQoygUQpom'], 
        u'merchant_email': [u'jitendra@gmail.com'], u'transaction_date': [u'06-06-2018']}>
    '''
    if request.method == 'POST':

        final_response = easebuzzObj.transactionDateAPI(request.POST)
        # return HttpResponse(final_response)
        return render(request, 'response.html', {'response_data': final_response})
    else:
        return render(request, 'transaction_date.html')


'''
* Use refund API
'''
def refund(request):
    '''
    * Very Important Notes
    *
    * Post Data should be below formate.

        <QueryDict: {u'txnid': [u'T300'], u'refund_amount': [u'0.9'], 
        u'phone': [u'1231231235'], u'amount': [u'1.03'], 
        u'csrfmiddlewaretoken': [u'rafbLZiPT3s6oP2uTqAyhjeViCr8gXP9DHyDcvtL52cGjRfMY4p85Wb9RBfu9NQ8'], 
        u'email': [u'jitendra@gmail.com']}>
    '''
    if request.method == 'POST':

        final_response = easebuzzObj.refundAPI(request.POST)
        # return HttpResponse(final_response)
        return render(request, 'response.html', {'response_data': final_response})
    else:
        return render(request, 'refund.html')


'''
* Use payout API
'''
def payout(request):
    '''
    * Very Important Notes
    *
    * Post Data should be below formate.

        <QueryDict: {u'csrfmiddlewaretoken': [u'4SGfTPO2B5mnq5rQ0lOcY5M0jw4X6FkhgpZHklZYN46Xl7E85ZDMMIJeSvSjZvlg'], 
        u'merchant_email': [u'jitendra@gmail.com'], u'payout_date': [u'06-06-2018']}>
    '''
    if request.method == 'POST':

        final_response = easebuzzObj.payoutAPI(request.POST)
        # return HttpResponse(final_response)
        return render(request, 'response.html', {'response_data': final_response})
    else:
        return render(request, 'payout.html')


'''
* Use response API
'''
def response(request):
    final_response = easebuzzObj.easebuzzResponse(request.POST)
    return render(request, 'response.html', {'response_data': final_response})
