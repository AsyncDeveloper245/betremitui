from django import forms
from django.forms.widgets import HiddenInput
from baxi_api.betremit_misc import GenerateReference
plan_options = (
    ('prepaid','prepaid'),
    ('postpaid','postpaid'),
)

service_type = (
    ('mtn','mtn'),
    ('glo','glo'),
    ('9mobile','9mobile'),
    ('airtel','airtel'),
    ('smile','smile')
)

class AirtimePurchaseForm(forms.Form):
    service_type = forms.ChoiceField(label='Service Provider',choices=service_type)
    amount = forms.IntegerField(label='Enter Amount')
    phone = forms.CharField(max_length=11,label='Enter Phone Number')
