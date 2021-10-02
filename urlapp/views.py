from django.shortcuts import render
from django.utils.crypto import get_random_string #to get the random string
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  UrlShoartner


# Create your views here.
def name2(request):
    var=get_random_string(length=10)
    return HttpResponse(var)

@api_view(['POST'])
def put(request):
    var1=request.data['url']
    unr=get_random_string()
    obj1=UrlShoartner(url=var1, shorturl=unr)
    obj1.save()
    return Response(unr)

def sample(request,su):
    short_url=su
    data=UrlShoartner.objects.get(shorturl=short_url)
    data2=data
    return redirect(data2.url)
