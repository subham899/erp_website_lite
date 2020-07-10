from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from . models import Customer_info
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    return render(request, 'home_app/index.html')

def newabout(request):
    return render(request, 'website/about.html')

def service(request):
    return render(request, 'website/serviceapp.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')

def team(request):
    return render(request, 'website/team.html')
def contact(request):
    if request.method == "POST":
        erp_name = request.POST['name']
        erp_massege = request.POST['message']
        send_mail(
            'NEW ERP WEBSITE',
            erp_massege,
            settings.EMAIL_HOST_USER,
            ['subhambasu980@gmail.com'],

            fail_silently=False,
        )

        return render(request, 'website/contact.html', {'erp_name': erp_name})
    else:
        return render(request, 'website/contact.html')





