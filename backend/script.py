import requests
import urllib
import json
from dotenv import load_dotenv
import os

# #TODO: Bring input from react
state = input("Please add the state acronym (ex. FL)") 
city= input("Please add the city (optional)")    

def rentcastApiCall(cityinput, state):
    
    #TODO: Bring input from react
    # state = input("Please add the state acronym (ex. FL)") 
    # city= input("Please add the city (optional)")    

    city = ''

    # Create query string; create a function that can be applied to other values
    for i in range(len(cityinput)):
        if cityinput[i] == " ":
            city+="%20"
            continue
        city += cityinput[i]
        
    url_q = "city="+city+"&state="+state

    url = "https://api.rentcast.io/v1/listings/rental/long-term?"+url_q

    #TODO: Modify to pass key from .env file
    api_key = os.getenv('RENTCAST_API_KEY')

    headers = {
        "accept": "application/json",
        "X-Api-Key": api_key # TODO: Pass API key safer
    }

    # Call API
    response = requests.get(url, headers=headers)

    # Add response as text data
    data = response.text

    # Load json data into a variable
    with open("sample.json", "w") as openfile:
        openfile.write(data)

def analyzeRentData():

    loopCounter = 0 
    jsonObjectNumber = 0
    list_counter=0

    # print(os.getcwd())
    averagePricePerSQFT=0

    # Open the sample file
    with open("sample.json", "r") as openfile: 
        json_object = json.load(openfile)

        rentalSampleDict = {}
        rentalPricePerSQFT = []
        while loopCounter < 15:
            try: 
                address = json_object[jsonObjectNumber]["addressLine1"]
                price = json_object[jsonObjectNumber]["price"]
                
                if not (json_object[jsonObjectNumber].get('squareFootage') is None):
                    sqft = json_object[jsonObjectNumber]["squareFootage"]
                    pricePerSqft=round(price/sqft, 2)
                    rentalPricePerSQFT.insert(list_counter,pricePerSqft) #TODO: Pass each one to front end or field on API
                    rentalSampleDict = {"address":address, "price":price, "size":sqft, "pricesqft":rentalPricePerSQFT[list_counter]}
                    averagePricePerSQFT += pricePerSqft 
                    loopCounter+=1
                    list_counter+=1
                
                    # print (rentalSampleDict) #TODO: Pass to Table in front end
                
                jsonObjectNumber+=1
            except IndexError:
                break
        
        averagePricePerSQFT= round(averagePricePerSQFT/list_counter, 2)
        
        return (rentalSampleDict, averagePricePerSQFT)

# rentcastApiCall(city,state)
# print (analyzeRentData())







