from django import forms

plan_options = (
    ('prepaid','prepaid'),
    ('postpaid','postpaid'),
)

class AirtimePurchaseForm(forms.Form):
    agentReference = forms.CharField(max_length=35)
    plan = forms.ChoiceField(choices = plan_options)
    service_type = forms.CharField(max_length=7)
    amount = forms.IntegerField()
    phone = forms.CharField(max_length=11)
