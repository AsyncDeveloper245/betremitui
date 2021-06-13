from django.shortcuts import render
from django.views.generic import TemplateView

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

class AirtimeView(TemplateView):
    template_name = 'airtime.html'

class ElectricityView(TemplateView):
    template_name = 'electricity.html'


class InternetSubView(TemplateView):
    template_name = 'internet_sub.html'


class OtpView(TemplateView):
    template_name = 'verify_otp.html'

class DataView(TemplateView):
    template_name  = 'data.html'