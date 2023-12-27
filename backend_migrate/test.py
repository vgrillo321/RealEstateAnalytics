import rentalanalyticsscript as script

state = input("Please add the state acronym (ex. FL)") 
cityinput= input("Please add the city (optional)")

script.rentcastApiCall(cityinput, state)
sample, p = script.insertSampleRentData()

print(sample.count())
print (p)
