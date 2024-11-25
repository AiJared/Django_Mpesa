from django.shortcuts import render
from django.http import HttpResponse
from .mpesa import AccessToken, Password

import requests
# Create your views here.

def home(request):
    return render(request, 'home.html')

def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        amount = request.POST["amount"]
        access_token = AccessToken.access_token
        apiurl = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        header = {"Authorization": "Bearer %s" % access_token}

        request = {    
            "BusinessShortCode": Password.shortcode,    
            "Password": Password.decoded_password,    
            "Timestamp":Password.timestamp,    
            "TransactionType": "CustomerPayBillOnline",    
            "Amount": amount,    
            "PartyA":phone,    
            "PartyB":Password.shortcode,    
            "PhoneNumber":phone,    
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa",    
            "AccountReference":"AiJared",    
            "TransactionDesc":"Payment to AiJared"
            }

    response = requests.post(apiurl, json=request, headers=header)
    return HttpResponse("success")
