import datetime

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    our_services = ['home designs', 'ui/ux' 'web developer']
    prices = 20000
    date = datetime.date.today()
    return render(request, 'services.html',
                  {'services': our_services, 'date': date, 'prices': prices})
