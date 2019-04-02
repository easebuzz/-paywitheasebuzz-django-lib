# paywitheasebuzz-python-django-lib-python2.7
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

# easebuzz documentation for kit integration
https://docs.easebuzz.in/

# paywitheasebuzz-python-django-lib kit, try it your self
*Once set up python environment then follow below steps*
1. clone paywitheasebuzz-python-django-lib on your's system.
2. unzip paywitheasebuzz-python-django-lib.
3. using virtual environment
    1. go to your's python environment folder using terminal or command prompt.
      
       1. active environment using below command.
           ```
               source bin/activate
           ```
       2. goto paywitheasebuzz-python-django-lib kit folder and run command like
            ```
                python manage.py runserver
            ```
       3. type URL: http://127.0.0.1:8000/
       
4. without virtual environment
    1. goto paywitheasebuzz-python-django-lib kit folder.
        1. run the below command.
        ```
            python manage.py runserver
        ```
        2. type URL: http://127.0.0.1:8000/

# Process for integrating paywitheasebuzz-python-django-lib kit in "Project"

1. copy and paste easebuzz_lib folder in your's project directory.
2. include easebuzz_payment_gateway.py file in your's views.py file.
    ```
        from easebuzz_lib.easebuzz_payment_gateway import Easebuzz
    ```
3. set MERCHANT_KEY, SALT, and ENV.
    ```
        MERCHANT_KEY = "10PBP71ABZ2";
        SALT = "ABC55E8IBW";         
        ENV = "test";   // "test for test enviroment or "prod" for production enviroment
    ```
4. create Easebuzz class object and pass MERCHANT_KEY, SALT and ENV.
    ```
        easebuzzObj = Easebuzz(MERCHANT_KEY, SALT, ENV)
    ```
5. call Easebuzz class methods or function based on your's requirements.
    1. Initiate Payment API
        *POST Format and call initiatePaymentAPI*
        ```
        postDict = {
            'txnid': 'T3SAT0B5OL',
            'firstname': 'jitendra',
            'phone': '1231231235',
            'email': 'jitendra@gmail.com'
            'amount': '1.03',
            'productinfo': 'Apple Mobile',
            'surl': 'http://localhost:8000/response/',
            'furl': 'http://localhost:8000/response/',
            'city': 'aaaa',
            'zipcode': '123123',
            'address2': 'aaaa',
            'state': 'aaaa',
            'address1': 'aaaa',
            'country': 'aaaa',
            'udf1': 'aaaa',
            'udf2': 'aaaa',
            'udf3': 'aaaa',
            'udf4': 'aaaa',
            'udf5': 'aaaa'
        }

        final_response = easebuzzObj.initiatePaymentAPI(postDict)
        result = json.loads(final_response)
        if result['status'] == 1:

            # note: result['data'] - contain payment link. 
            return redirect(result['data'])
        else:
            return render(request, 'response.html', {'response_data': final_response})
        ```
    2. Transaction API
        *POST Format and call transactionAPI*
        ``` 
        postDict = {
            'txnid':'T300',
            'amount':'1.03',
            'phone':'1231231235',
            'email':'jitendra@gmail.com'
        }

        final_response = easebuzzObj.transactionAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})
        ```
    3. Transaction API (by date)
        *POST Format and call transactionDateAPI*
        ```
        postDict = {
            'merchant_email':'jitendra@gmail.com',
            'transaction_date':'06-06-2018'
        }

        final_response = easebuzzObj.transactionDateAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})
        ```
    4. Refund API
        *POST Format and call refundAPI*
        ```
        postDict = {
            'txnid':'T300',
            'refund_amount':'0.9',
            'phone':'1231231235',
            'amount':'1.03',
            'email':'jitendra@gmail.com'
        }

        final_response = easebuzzObj.refundAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})    
        ```
    5. Payout API
        *POST Format and call payoutAPI*
        ```
        postDict = {
            'merchant_email':'jitendra@gmail.com',
            'payout_date':'06-06-2018'
        }

        final_response = easebuzzObj.payoutAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})
        ```
    6. Response of Inititate Payment API
    
        *Initiate Payment API response will be sent on success URL or failure URL using HTTP form post.*

        ```
            final_response = easebuzzObj.easebuzzResponse(request.POST)
            return render(request, 'response.html', {'response_data': final_response})
        ```