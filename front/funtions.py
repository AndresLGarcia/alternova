from supabase.client import create_client, Client
from supabase import create_client
from decouple import config
import requests
from .views import *


def enviocorreo(email):
    supabase: Client = create_client(config("SUPABASE_URL"), config("SUPABASE_KEY"))
    user = supabase.auth.sign_up(email=email, password="aleatorio**")
    return user.id


def peticionchiste(uuid):
    if uuid:
        url = "https://api.chucknorris.io/jokes/random"
        data = requests.get(url)
        value = ""
        if data.status_code == 200:
            value = data.json()
            return value
    return "user No logueado"


def getdatajoke(id):
    url = f"https://api.chucknorris.io/jokes/{id}"
    data = requests.get(url)
    if data.status_code == 200:
        value = data.json()
        return value
