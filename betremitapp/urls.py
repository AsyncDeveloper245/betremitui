from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.homepageView.as_view(),name='home'),
    path('transfer/',views.TransferView.as_view(),name='transfer'),
    path('online_payment/',views.OnlinePaymentView.as_view(),name='online_payment'),
    path('success/',views.SuccessPageView.as_view(),name='success_page'),
    path('error/',views.ErrorPageView.as_view(),name='error_page'),
    path('virtual_card/',views.VirtualCardView.as_view(),name='virtual_card'),
    path('airtime/',views.AirtimeView.as_view(),name='airtime'),
    path('electricity/',views.ElectricityView.as_view(),name='electricity'),
    path('internet_subscription/',views.InternetSubView.as_view(),name='internet_sub'),
    path('data/',views.DataView.as_view(),name='data'),
    # path('code_error/',views.homepageView.as_view(),name='code_error'),
    path('verify-otp/',views.OtpView.as_view(),name='otp'),

]