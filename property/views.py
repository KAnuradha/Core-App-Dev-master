from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# import requests
# from xml.etree import ElementTree as ET
# from xml.etree.ElementTree import fromstring
# from xmljson import badgerfish as bf
# from json import dumps
# import json as simplejson

from django.db.models import Q
from .models import Property_details
from .serializer import PropertySerializer


# Create your views here.
def main(request):
	return render(request,'index1.html')


def show(request):
	if request.method == "POST":
		l=['novel tech','kudlu gate','banglore','karnataka',560068,10,3,12,'2000sqrt']
		return render(request,'edit_your_property.html', {'data':l})


# address="address"
# citystatezip="your zipcode"
# url = "http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19lq7ppy70r_305s0&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA";
# response = requests.get(url)
# print(response.status_code)
# c = response.content
# d = bf.data(fromstring(c))
# e = dumps(d)
# print e

# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def save_property(request):
# 	if request.method == "POST":
# 		property_title = request.POST.get("property_title")
# 		print request.POST.get("property_title")
# 		# obj = Property_details.objects.filter(Q(property_title=property_title))
# 		# if obj:
# 		# 	print request.POST.get("property_title")
# 		# 	return HttpResponse("this property is already exist")
#   #       else:
#         serializer = PropertySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return render(request,'my_properties.html')




def save_property(request):
	if request.method == "POST":
		prty = request.POST.get('property_title')
		o = Property_details.objects.filter(property_title=prty)
		if o:
			return HttpResponse("this property is already exist")
		else:	
			obj=Property_details(
			property_title = request.POST.get('property_title'),
			address = request.POST.get('address'),
			city = request.POST.get('city'),
			state = request.POST.get('state'),
			zip_code = request.POST.get('zip_code'),
			home_type = request.POST.get('home_type'),
			beds = request.POST.get('beds'),
			baths =request.POST.get('baths'),
			rooms = request.POST.get('rooms'),
			property_size = request.POST.get('property_size'),
			description = request.POST.get('description'),
			other_features = request.POST.get('other_features'))
			obj.save()
			l = [request.POST.get('property_title'),request.POST.get('address'),request.POST.get('city'),request.POST.get('state'),request.POST.get('beds'),request.POST.get('baths'),request.POST.get('property_size')]
			return render(request,'my_properties.html',{'data':l})