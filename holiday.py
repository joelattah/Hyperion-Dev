
def hotel_cost(num_nights): #function called hotel_cost has one parameter, num_nights
    hotel_expense  = num_nights * 40 #multiply number of nights by daily rate of £40
    return hotel_expense #return hotel_expense value


def plane_cost(city_flight):#function called plane_cost has one parameter, city_flight
    if city_flight in city_list:
        #this obtains the corresponding price (value) for the chosen country (key) from the dictionary city_prices
        plane_expense = city_prices[city_flight]
    else:
        print("Flight not available")

    return plane_expense  #returns plane cost value


def car_rental(rental_days):#function called car_rental has one parameter, rental_days
    rental_expense  = rental_days * 20 #multiply number of days by daily rate of £20
    return rental_expense #returns rental cost value


#function called holiday_cost has 3 parameters, hotel_expense, plane_expense, rental_expense
def holiday_cost(hotel_expense, plane_expense, rental_expense):
    finalhotel_cost = hotel_cost(num_nights) #create a variable to store the hotel cost returned from function
    finalplane_cost = plane_cost(city_flight) #create a variable to store the plane cost returned from function
    finalcar_cost = car_rental(rental_days) #create a variable to store the car rental cost returned from function
    total_cost =  finalhotel_cost + finalplane_cost + finalcar_cost #totals all costs

    return total_cost #returns total cost of holiday

#displays holiday destinations and prices to user
print("** City Prices **")
print("\t")
print("London - £800")
print("Paris - £685")
print("Milan - £480")

#list created to check destination and then check price in dictionary
list_destinations =['London', 'Paris', 'Milan'] 

# dictionary created so that city can be used as a key and then the price of flight as the value to be accessed
city_prices = {'London':800 , 
          'Paris': 685 , 
          'Milan': 480 , 
              } # dictionary created so that city can be used as a key and then the price of flight as the value to be accessed

#obtains user input to perform calculations for holiday costs
city_flight = input("From the options provided which city would you like to vist?: ")
num_nights = int(input("How many nights will you be staying at a hotel?: "))
rental_days = int(input("How many days will you be hiring a car?: "))

#the following variables plane_expense, hotel_expense, rental_expense are defined to be used in function holiday_cost(hotel_expense, plane_expense, rental_expense) 
plane_expense = plane_cost(city_flight) #create a variable to store the plane cost returned from function plane_cost(city_flight)
hotel_expense = hotel_cost(num_nights) #create a variable to store the hotel cost returned from function hotel_cost(num_nights)

#create a variable to store the car rental cost returned from function car_rental(rental_days)
rental_expense = car_rental(rental_days) 

#create a variable to store the total holiday cost returned from function holiday_cost(hotel_expense, plane_expense, rental_expense) 
holiday_expense = holiday_cost(hotel_expense, plane_expense, rental_expense) 

#output holiday details to user
print("\t")
print(f"Holiday Details : You will be travelling to {city_flight} for {num_nights} nights")
print("Flight Cost:", "£" + str(plane_expense))
print(f"Hotel : You will be staying in your hotel for {num_nights} nights at a cost of", "£"+ str(hotel_expense))
print(f"Car Rental : Your rental will be for {rental_days} days at a cost of", "£"+ str(rental_expense))
print("Total Holiday Cost:", "£" + str(holiday_expense))

