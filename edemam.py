import api_controller
import json
from pprint import pprint
import requests

url = 'https://api.edamam.com/api/food-database/v2/parser?'
key= 'bb5307a190c08e54fe63612f874be4f3'
#_id=2272dc20&app
#https://api.edamam.com/api/food-database/v2/parser?ingr=pepsi&app_id=2272dc20&app_key=bb5307a190c08e54fe63612f874be4f3

def get_drink():
    search_drink = ''.strip()
    while len (search_drink) == 0 or not search_drink.isalpha():
        search_drink = input('Search for a drink')
    return search_drink


def drink_query(drink, key):
    try: 
        query = {'query': drink, 'addDrinkInformation': 'name', 'fat': key}
        response = requests.get(url, params=query)
        data = response.json()
        pprint(data)
    except Exception as e:
        print('Error with query')





