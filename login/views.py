from django.shortcuts import render,render_to_response 
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.db.models import Q
from registration.models import HubreeUser,Hubree

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def home(request):
    return render(request,'login-signup-landing.html')

def accounts(request):
    return render(request, 'index.html')


def log_in(request):
    return render(request, 'login-form.html',{'data':''})

def main(request):
    return render(request, 'index1.html')

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
        result = Hubree.objects.filter(Q(email = email) & Q(password = password))
        if result:
            for rec in result:
                return render(request, 'my_properties.html')
                # if rec.verificationstatus:
                #     return render(request, 'index.html')
                # else:
                #     return render(request, 'signup-verification.html')
        else:
            return render(request, 'login-form.html', {'data':"Incorrect email address"})


def forgot(request):
    return render(request, 'reset-password.html')




@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def password(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        hubree = Hubree.objects.filter(email = email_id)
        for rec in hubree:
            rec.password = request.POST.get('password')
            rec.save()
        return render(request, 'login-form.html', {'data':'Your password is successfully changed'})
