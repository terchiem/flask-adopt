import random
import requests as HTTP_request
from secrets import PET_FINDER_API_KEY, PET_FINDER_SECRET




def request_pet_finder_token():
    """Request a new token for PetFinder API"""
    resp = HTTP_request.post('https://api.petfinder.com/v2/oauth2/token',
        data={
            "grant_type": 'client_credentials',
            "client_id": PET_FINDER_API_KEY,
            "client_secret": PET_FINDER_SECRET
        })
    return resp.json()["access_token"]

def get_random_pet():
    """Get a random pet from PetFinder API"""
    resp = HTTP_request.get(' https://api.petfinder.com/v2/animals',
          params={
            "limit": 100,
          },
          headers={"Authorization": f"Bearer {pet_finder_token}"})

    pets = resp.json()["animals"]

    random_pet = random.choice(pets)

    return {"name": random_pet["name"], "age": random_pet["age"],  "photo_url": random_pet["photos"][0]["medium"]}

# PetFinder token, but will expire each hour
pet_finder_token = request_pet_finder_token()