import requests
import urllib
import json


# state = input("Please add the state acronym (ex. FL)") #TODO: Change to a lambda compatible input
# cityinput= input("Please add the city (optional)")     #TODO: Same
# city = ""

# Create query string; create a function that can be applied to other values
# for i in range(len(cityinput)):
#     if cityinput[i] == " ":
#         city+="%20"
#         continue
#     city += cityinput[i]
    
# url_q = "city="+city+"&state="+state

# url = "https://api.rentcast.io/v1/listings/rental/long-term?"+url_q

# headers = {
#     "accept": "application/json",
#     "X-Api-Key": "4bbec6c728f54cfd9e408d03c65e9870" # TODO: Pass API key safer
# }

# Call API
# response = requests.get(url, headers=headers)

# Add response as text data
# data = response.text

#Pass Json data to List or Dictionary if it contains the squareFootage
row_counter = 9 #TODO: add as input
jsonObjectNumber = 0

with open("test_data.json", "r") as openfile: #TODO:change to sample.json when using API
    json_object = json.load(openfile)

rentalSampleDict = {"address":"", "price":0, "size":0, "pricesqft":0}
rentalPricePerSQFT = []
while row_counter < 2:

    address = json_object[jsonObjectNumber]["addressLine1"]
    price = json_object[jsonObjectNumber]["price"]
    
    if not (json_object[jsonObjectNumber].get('squareFootage') is None):
        sqft = json_object[jsonObjectNumber]["squareFootage"]
        pricePerSqft=price/sqft
        rentalPricePerSQFT.insert(pricePerSqft) #TODO: Pass each one to front end or field on API
        row_counter+=1
    
    rentalSampleDict = {"address":address, "price":price, "size":sqft, "pricesqft":rentalPricePerSQFT}
    print (rentalSampleDict)
    jsonObjectNumber+=1
 


print (rentalPricePerSQFT)






