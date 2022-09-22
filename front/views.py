from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from django.http import HttpResponse
from decouple import config
from .funtions import *
from django.http import JsonResponse
import json
from .serializers import *
from .api import ProjectviewSet


class HttpResponseNoContent(HttpResponse):
    status_code = 204


def home(request):
    return render(request, "home.html")


def login(request):
    return render(request, "login.html")


def jokes(request):
    email = request.GET.get("email")
    emailregister = "algarcia677@misena.edu.co"
    mensaje = "User No register please login"
    if email != emailregister:
        return render(request, "login.html", {"mensaje": mensaje})
    else:
        uuid = enviocorreo(email)
        return render(request, "getJokes.html", {"user": uuid, "email": email})


def getjokes(_request, uuid):
    data = peticionchiste(uuid)
    return JsonResponse(data)

def myjokes(request,email):
    url = f"https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products?user=eq.{email}&select=*"

    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        values = []
        for i in data:
            values.append(i.get('value'))
        return render(request, "myJokes.html", {"values" : values, "user": email })

    except Exception as err:
        print(err)
        return render(request, "myJokes.html")



def addjoke(_request, ur, email):

    date = getdatajoke(ur)
    url = "https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products"
    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }
    data = {
        "idChiste": date.get("id"),
        "value": date.get("value"),
        "url": date.get("url"),
        "user": email,
    }
    try:
        response = requests.post(url=url, json=data, headers=headers)
        return JsonResponse(response, safe=False)
    except Exception as err:
        print(response)
        return JsonResponse(err)


@api_view(["GET"])
def listjokes(_request):

    url = "https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products?select=*"

    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }
    try:
        response = requests.get(url, headers=headers)
        return JsonResponse(response.json(), safe=False)
    except Exception as err:
        print(err)


@api_view(["GET"])
def listjoke(_request, user):

    url = f"https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products?user=eq.{user}&select=*"

    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }
    try:
        response = requests.get(url, headers=headers)
        return JsonResponse(response.json(), safe=False)
    except Exception as err:
        print(err)


@api_view(["PATCH"])
def updatejoke(request, ids):
    values = request.body.decode("utf-8")
    body = json.loads(values)

    url = f"https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products"
    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }

    params = {"id": f"eq.{ids}"}
    print(body)
    try:
        response = requests.patch(url, json=body, params=params, headers=headers)
        if response.status_code == 204:
            return JsonResponse(response.status_code, safe=False)
    except Exception as err:
        return JsonResponse(err.response.status_code)


@api_view(["DELETE"])
def deletejoke(request, ids):
    url = f"https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products"
    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }
    params = {"id": f"eq.{ids}"}
    try:
        response = requests.delete(url=url, params=params, headers=headers)
        return JsonResponse(response.status_code, safe=False)
    except Exception as err:
        return JsonResponse(err)


@api_view(["POST"])
def createjoke(request):
    values = request.body.decode("utf-8")
    body = json.loads(values)

    url = "https://pqgqtixklmpmahgbiboa.supabase.co/rest/v1/products"
    headers = {
        "Content-Type": "application/json",
        "Authorization": config("JWT"),
        "apikey": config("API_KEY"),
    }
    data = {
        "idChiste": body["idChiste"],
        "value": body["value"],
        "url": body["url"],
        "user": body["user"],
    }
    try:
        response = requests.post(url=url, json=data, headers=headers)
        print(response)
        return JsonResponse(response.status_code, safe=False)
    except Exception as err:
        return JsonResponse(err)
