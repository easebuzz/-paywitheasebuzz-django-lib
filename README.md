# paywitheasebuzz-python-django-lib
Python-Django integration kit for pay with easebuzz pay.easebuzz.in

# Software Requirement
*setup python-django kits on test/development/production environment install below software*
1. pip
2. python 2.7
3. Django 1.11
4. requests 2.18.4

# Note: 
*We strongly recommend to set up this kits inside virtual environment to avoid any conflict with your's existing projects.*
1. virtualenv 


# easebuzz Documentation for kit integration
https://docs.easebuzz.in/

# Process for test paywitheasebuzz-python-django-lib kit
*Once set up python environment then follow below steps*
1. clone paywitheasebuzz-python-django-lib on your's system.
2. unzip paywitheasebuzz-python-django-lib.
3. if set up virtual environment
    1. goto your's python environment folder using terminal or command prompt.
        ENV/python27_django_1_11_13/ 
       1. active enviroments using below command.
               ```
                   source bin/activate
               ```
       2. goto paywitheasebuzz-python-django-lib kit folder and run command like
            (python27_django_1_11_13) abc@abc:~/Python_Project/ENV/python27_django_1_11_13/
            ```
                python manage.py runserver
            ```
       3. type URL: http://127.0.0.1:8000/
       
    2. goto kit directory.
        python27_django_1_11_13/
        1. run the below command.
        ```
            python manage.py runserver
        ```
        2. type URL: http://127.0.0.1:8000/


# Process for integrating paywitheasebuzz-python-django-lib kit in "Project"

1. Copy and Paste easebuzz_lib folder in your's project directory.
2. include easebuzz_payment_gateway.py file in your's views.py file.
    ```
        from easebuzz_lib.easebuzz_payment_gateway import Easebuzz
    ```
3. set MERCHANT_KEY, SALT, and ENV.
    ```
        MERCHANT_KEY = "10PBP71ABZ2";
        SALT = "ABC55E8IBW";         
        ENV = "test";   // set enviroment name
    ```
4. create Easebuzz class object and pass MERCHANT_KEY, SALT and ENV.
    ```
        easebuzzObj = Easebuzz(MERCHANT_KEY, SALT, ENV)
    ```
5. call Easebuzz class methods and function based on your's requirements.
    1. Initiate Payment API
        *POST Format*
        ```
        <QueryDict: {u'city': [u'aaaa'], u'zipcode': [u'123123'], u'address2': [u'aaaa'], 
        firstname': [u'jitendra'], u'state': [u'aaaa'], u'address1': [u'aaaa'], 
        u'surl': [u'http://localhost:8000/response/'], u'udf3': [u'aaaa'], 
        u'txnid': [u'T3SAT0B5OL'], u'productinfo': [u'Apple Mobile'], 
        u'furl': [u'http://localhost:8000/response/'], u'udf1': [u'aaaa'], 
        u'phone': [u'1231231235'], u'amount': [u'1.03'], u'udf2': [u'aa'], 
        u'udf5': [u'aaaa'], u'udf4': [u'aaaa'], u'country': [u'aaaa'], 
        u'csrfmiddlewaretoken': [u'6zKwuxucnwd3J2CXcFR3lj0nW8eiL8Y0i63YV3F8zvXDE4PfhjGD9WXBv72EEYZZ'], 
        u'email': [u'jitendra@gmail.com']}>
        ```
        *call initiatePaymentAPI*
        ```
            final_response = easebuzzObj.initiatePaymentAPI(request.POST)
            result = json.loads(final_response)
            if result['status'] == 1:
                return redirect(result['data'])
            else:
                return render(request, 'response.html', {'response_data': final_response}
        ```
    2. Transaction API
        *POST Format*
        ```
        <QueryDict: {u'phone': [u'1231231235'], 
        u'csrfmiddlewaretoken': [u'X1vgdvX5eJfDeQSUx12XMuPxYmBTExTq9yOIE181qIZd9S5cCFRxA7MLxlpfxnUp'], 
        u'txnid': [u'T300'], u'amount': [u'1.03'], u'email': [u'jitendra@gmail.com']}>
        ```
        *call transactionAPI*
        ```
            final_response = easebuzzObj.transactionAPI(request.POST)
            return render(request, 'response.html', {'response_data': final_response})
        ```
    3. Transaction API (by date)
        *POST Format*
        ```
        <QueryDict: {u'csrfmiddlewaretoken': [u'aQArNZMurJD9bPrWYRmZohRCPzsyXznnmnTTevXqDInJ6REe3vbzcUOQoygUQpom'], 
        u'merchant_email': [u'jitendra@gmail.com'], u'transaction_date': [u'06-06-2018']}>
        ```
        *call transactionDateAPI*
        ```
            final_response = easebuzzObj.transactionDateAPI(request.POST)
            return render(request, 'response.html', {'response_data': final_response})
        ```
    4. Refund API
        *POST Format*
        ```
        <QueryDict: {u'txnid': [u'T300'], u'refund_amount': [u'0.9'], 
        u'phone': [u'1231231235'], u'amount': [u'1.03'], 
        u'csrfmiddlewaretoken': [u'rafbLZiPT3s6oP2uTqAyhjeViCr8gXP9DHyDcvtL52cGjRfMY4p85Wb9RBfu9NQ8'], 
        u'email': [u'jitendra@gmail.com']}>
        ```
        *call refundAPI*
        ```
            final_response = easebuzzObj.refundAPI(request.POST)
            return render(request, 'response.html', {'response_data': final_response})    
        ```
    5. Payout API
        *POST Format*
        ```
        <QueryDict: {u'csrfmiddlewaretoken': [u'4SGfTPO2B5mnq5rQ0lOcY5M0jw4X6FkhgpZHklZYN46Xl7E85ZDMMIJeSvSjZvlg'], 
        u'merchant_email': [u'jitendra@gmail.com'], u'payout_date': [u'06-06-2018']}>
        ```
        *call payoutAPI*
        ```
            final_response = easebuzzObj.payoutAPI(request.POST)
            return render(request, 'response.html', {'response_data': final_response})
        ```
    6. Response of Inititate Payment API
        ```
            final_response = easebuzzObj.easebuzzResponse(request.POST)
            return render(request, 'response.html', {'response_data': final_response})
        ```