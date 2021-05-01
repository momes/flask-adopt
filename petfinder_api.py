from flask import Flask, render_template, redirect, flash, request
from project_secrets import PETFINDER_API_KEY, PETFINDER_SECRET_KEY
import requests
from app import app

def get_api_token():
    resp = requests.post(
        "https://api.petfinder.com/v2/oauth2/token",
        data={"grant_type":"client_credentials", 
                "client_id": PETFINDER_API_KEY, 
                "client_secret": PETFINDER_SECRET_KEY}
    )
    token = resp.json()
    token = token["access_token"]
    return token

def get_random_pets():
    token = get_api_token()
    resp = request.get("https://api.petfinder.com/v2/animals",
    params={"Authorization": f"Bearer {token}", "limit":"100"})

    animals = resp.json()

    return animals
