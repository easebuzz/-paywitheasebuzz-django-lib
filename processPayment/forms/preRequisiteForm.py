__author__ = 'jaishankar'


from django import forms
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import MaxLengthValidator


class PayWithEasebuzzPreRequisiteForm(forms.Form):
    amount = forms.CharField(validators=[RegexValidator(r'[0-9]')],required=True, help_text="Enter Amount", widget=forms.TextInput(attrs={'class': 'validate','placeholder':'Enter Amount','type':'number'}))
    payer = forms.CharField(validators=[RegexValidator(r'[a-zA-Z]')],required=True, help_text="Enter Your Name", widget=forms.TextInput(attrs={'class': 'validate','placeholder':'Enter Your Name'}))
    email = forms.CharField(validators=[EmailValidator()], required=True, help_text="Enter Your Email",widget=forms.TextInput(attrs={'class': 'validate','placeholder':'Enter Your email','type':'email'}))
    phone = forms.CharField(validators=[RegexValidator(r'[0-9]{10}', message='Please enter a valid phone number'), MaxLengthValidator(10,message='Please enter a 10 digits long phone number')],required=True, help_text="Enter Phone",widget=forms.TextInput(attrs={'class': 'validate','placeholder':'Enter phone number','maxlength':'10','minlength':'10'}))


    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data