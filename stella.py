from urllib import response
import requests
from pushbullet import Pushbullet
from dotenv import load_dotenv
from os import environ

load_dotenv()

pb = Pushbullet(environ['PBKEY'])

PRODUCT_ID = "369"
PLACE_ID = "620"
API = "https://ecgproductmw.colruyt.be/ecgproductmw/v2/nl/products/" + PRODUCT_ID + "?clientCode=clp&placeId=" + PLACE_ID

print(API)
response = requests.get(API)
data = response.json()
price = data["price"]["basicPrice"]
isRedPrice = data["price"]["isRedPrice"]
inPromotion = data["inPromo"]
try:
    quantityPrice = data["price"]["quantityPrice"]
except KeyError:
    quantityPrice = False
if(isRedPrice):
    pb.push_note("🚨 Rode prijs op de Stella! 🚨", "Wow de Stella is een rode prijs! De nieuwe prijs is: " + str(price) + " euro")
elif(inPromotion):
    pb.push_note("🚨 Korting op de Stella 🚨", "Wow de Stella is in de korting klik op de link om te zien wat er te winnen valt! De nieuwe prijs is: " + str(price) + " euro \n\
        https://www.colruyt.be/nl/producten/pils-5-2-vol-5006")
elif(quantityPrice):
    pb.push_note("🚨 volume korting op de Stella 🚨", "Volume korting op stella: €{} per bak!".format(quantityPrice))
