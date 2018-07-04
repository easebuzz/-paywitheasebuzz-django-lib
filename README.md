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
5. call Easebuzz class methods and function based on your's requirements.
    1. Initiate Payment API
        *POST Format and call initiatePaymentAPI*
        ```
        postDict = {
            'city': 'aaaa',
            'zipcode': '123123',
            'address2': 'aaaa',
            'firstname': 'jitendra',
            'state': 'aaaa',
            'address1': 'aaaa',
            'surl': 'http://localhost:8000/response/',
            'udf3': 'aaaa',
            'txnid': 'T3SAT0B5OL',
            'productinfo': 'Apple Mobile',
            'furl': 'http://localhost:8000/response/',
            'udf1': 'aaaa',
            'phone': '1231231235',
            'amount': '1.03',
            'udf2': 'aaaa',
            'udf5': 'aaaa',
            'udf4': 'aaaa',
            'country': 'aaaa',
            'csrfmiddlewaretoken': '6zKwuxucnwd3J2CXcFR3lj0nW8eiL8Y0i63YV3F8zvXDE4PfhjGD9WXBv72EEYZZ',
            'email': 'jitendra@gmail.com'
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
            'phone':'1231231235',
            'csrfmiddlewaretoken':'X1vgdvX5eJfDeQSUx12XMuPxYmBTExTq9yOIE181qIZd9S5cCFRxA7MLxlpfxnUp',
            'txnid':'T300',
            'amount':'1.03',
            'email':'jitendra@gmail.com'
        }

        final_response = easebuzzObj.transactionAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})
        ```
    3. Transaction API (by date)
        *POST Format and call transactionDateAPI*
        ```
        postDict = {
            'csrfmiddlewaretoken':'aQArNZMurJD9bPrWYRmZohRCPzsyXznnmnTTevXqDInJ6REe3vbzcUOQoygUQpom',
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
            'csrfmiddlewaretoken':'rafbLZiPT3s6oP2uTqAyhjeViCr8gXP9DHyDcvtL52cGjRfMY4p85Wb9RBfu9NQ8',
            'email':'jitendra@gmail.com'
        }

        final_response = easebuzzObj.refundAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})    
        ```
    5. Payout API
        *POST Format and call payoutAPI*
        ```
        postDict = {
            'csrfmiddlewaretoken':'4SGfTPO2B5mnq5rQ0lOcY5M0jw4X6FkhgpZHklZYN46Xl7E85ZDMMIJeSvSjZvlg',
            'merchant_email':'jitendra@gmail.com',
            'payout_date':'06-06-2018'
        }

        final_response = easebuzzObj.payoutAPI(postDict)
        return render(request, 'response.html', {'response_data': final_response})
        ```
    6. Response of Inititate Payment API
        *Note: request.POST - means holds Initiate Payment API response*

        ```
            final_response = easebuzzObj.easebuzzResponse(request.POST)
            return render(request, 'response.html', {'response_data': final_response})
        ```