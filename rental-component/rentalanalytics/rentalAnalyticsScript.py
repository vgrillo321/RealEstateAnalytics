import requests
import urllib
import json
import os
# from dotenv import load_dotenv
# from members.models import Member

# city = ''
# state = ''
# rentcastApiCall(city,state)



def rentcastApiCall(city, state):
    
#TODO: Bring input from react
    # stateinput = state       # input("Please add the state acronym (ex. FL)") 
    cityInput = city              # input("Please add the city (optional)") 
    cityNoSpace = ''

    
    if cityInput != '':
    # Create query string; create a function that can be applied to other values
        for i in range(len(cityInput)):
            if cityInput[i] == " ":
                cityNoSpace+="%20"
                continue
            cityNoSpace += cityInput[i]
            
        url_q = "city="+cityNoSpace+"&state="+state
    else: 
        url_q = "&state="+state

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
        openfile.close()

def insertSampleRentData():

    loopCounter = 0 
    jsonObjectNumber = 0
    list_counter=0

    # print(os.getcwd())
    averagePricePerSQFT=0

    # Open the sample file
    with open("sample.json", "r") as openfile: 
        json_object = json.load(openfile)

        rentalSample = []
        rentalPricePerSQFT = []
        objectCount = len(json_object)

        try:
            while loopCounter < objectCount:
                try: 
                    address = json_object[jsonObjectNumber]["addressLine1"]
                    price = json_object[jsonObjectNumber]["price"]
                    
                    if not (json_object[jsonObjectNumber].get('squareFootage') is None):
                        sqft = json_object[jsonObjectNumber]["squareFootage"]
                        pricePerSqft=round(price/sqft, 2)
                        rentalPricePerSQFT.insert(list_counter,pricePerSqft) #TODO: Pass each one to front end or field on API
                        rentalSample += [{"address":address, "price":price, "size":sqft, "pricesqft":rentalPricePerSQFT[list_counter]}]
                        averagePricePerSQFT += pricePerSqft 
                        loopCounter+=1
                        list_counter+=1
                    
                        # print (rentalSampleDict) #TODO: Pass to Models in Django Database
                    
                    jsonObjectNumber+=1
                except IndexError:
                    break
        except KeyError:
            return()

        
        sortedPricePerSqft = sorted(rentalPricePerSQFT)
        
        maxPricePerSQFT = sortedPricePerSqft[len(sortedPricePerSqft)-1]
        minPricePerSQFT = sortedPricePerSqft[0]
        averagePricePerSQFT= round(averagePricePerSQFT/list_counter, 2)
        return (rentalSample, averagePricePerSQFT, maxPricePerSQFT, minPricePerSQFT)


# Calls for testing
# city = 'Oxon Hill'
# state = 'MD'
# Call rent cast APU NOTE: This may inquire cost, use carefully
#rentcastApiCall(city, state)

# NOTE: Prints de prueba
# sample , averagePricePerSQFT, maxPricePerSQFT, minPricePerSQFT = insertSampleRentData()
# print (sample)
# print ("---------------------------------------------------")
# print (f"Analyzed an amount of {len(sample)} rental listings in {city}")
# print ("---------------------------------------------------")
# print (f"This is the min price per sqft: {minPricePerSQFT}")
# print (f"This is the average price per sqft: {averagePricePerSQFT}")
# print (f"This is the max price per sqft: {maxPricePerSQFT}")





