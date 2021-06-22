from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from baxi_api.betremit import Betremit
from baxi_api.betremit_misc import GenerateReference
from .forms import AirtimePurchaseForm


# Create your views here.
class homepageView(TemplateView):
    template_name = 'modal.html'

class TransferView(TemplateView):
    template_name = 'bank_transfer.html'

class OnlinePaymentView(TemplateView):
    template_name = 'card_payment.html'

class SuccessPageView(TemplateView):
    template_name = 'trans_success.html'


class ErrorPageView(TemplateView):
    template_name = 'trans_failure.html'

class VirtualCardView(TemplateView):
    template_name = 'virtual_card.html'


class ElectricityView(TemplateView):
    template_name = 'electricity.html'


class InternetSubView(TemplateView):
    template_name = 'internet_sub.html'


class OtpView(TemplateView):
    template_name = 'verify_otp.html'

class DataView(TemplateView):
    template_name  = 'data.html'



def AirtimeView(request):
    betremit = Betremit("5adea9-044a85-708016-7ae662-646d59")
    agentReference = str(GenerateReference())
    agentId = 207
    if request.method == 'GET':
        form = AirtimePurchaseForm()
        response = betremit.Airtime.service_providers()
        service_providers = response['data']['data']['providers']
        services = [service['service_type'] for service in service_providers]
        return render(request,'airtime.html',{"services":services,'agentReference':agentReference,"agentId":agentId,'form':form})

    if request.method == 'POST':
        plan = request.POST['plan']
        service = request.POST['service_type']
        amount = request.POST['amount']
        phone = request.POST['phone']
        payload = {
            'agentReference':agentReference,
            'agentId':207,
            'plan':plan,
            "amount":int(amount),
            "phone":phone,
            "service_type":service,
        }
        print(payload)
        response = betremit.Airtime.request_airtime(payload)
        print(response)

        if not response == None:
            return render(request,'trans_success.html')

        else:
            return render(request,'trans_failure.html')



    
    