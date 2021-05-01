
from project_secrets import PETFINDER_API_KEY, PETFINDER_SECRET_KEY
import requests
from random import choice

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

def get_random_pet():
    token = get_api_token()
    resp = requests.get("https://api.petfinder.com/v2/animals",
    headers={"Authorization": f"Bearer {token}"}, params={"limit":"100"})

    animals = resp.json()
    # print(animals["animal"])
    animal = animals["animals"]
    random_animal = choice(animal)
    name = random_animal["name"]
    photo = random_animal["primary_photo_cropped"]["medium"] if (random_animal["primary_photo_cropped"]) else None
    age = random_animal["age"]
    return {"name":name, "photo":photo, "age":age}
