import requests
import urllib
import json
# from dotenv import load_dotenv Enable when testing API call
import os

state = input("Please add the state acronym (ex. FL)") #TODO: Change to a lambda compatible input
cityinput= input("Please add the city (optional)")     #TODO: Same
city = ""

# def configure():
#     load_dotenv()

# Create query string; create a function that can be applied to other values
for i in range(len(cityinput)):
    if cityinput[i] == " ":
        city+="%20"
        continue
    city += cityinput[i]
    
url_q = "city="+city+"&state="+state

url = "https://api.rentcast.io/v1/listings/rental/long-term?"+url_q

# headers = {
#     "accept": "application/json",
#     "X-Api-Key": os.getenv('api-key') # TODO: Pass API key safer
# }

# Call API
# response = requests.get(url, headers=headers)

# Add response as text data
# data = response.text

#Pass Json data to spreadsheet if it contains the squareFootage
loopCounter = 0 #TODO: add as input depending on the sample data needed
jsonObjectNumber = 0
list_counter=0

# print(os.getcwd())
averagePricePerSQFT=0

with open("sample.json", "r") as openfile: #TODO:change to sample.json when using API
    json_object = json.load(openfile)

    rentalSampleDict = {}
    rentalPricePerSQFT = []
    while loopCounter < 15:

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
        
            print (rentalSampleDict)
        
        jsonObjectNumber+=1

print("Im outside the loop now ----------------------")
print(rentalSampleDict)
averagePricePerSQFT= round(averagePricePerSQFT/list_counter, 2)
print ("The average price per sqft in the area is: " + str(averagePricePerSQFT))






