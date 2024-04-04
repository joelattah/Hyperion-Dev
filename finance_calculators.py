""" A program that allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator. """

import math


    #prints out a menu display to allow the user to select calculator options
print ("Investment - to calculate the amount of interest you'll earn on your interest")
print ("Bond       - to calculate the amount you'll have to pay on a home loan ")
print("\n")
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")


    #Checks if user input was "investment" and provides corresponding info and performs revelant calculations
if user_choice.lower() == "investment":
    print("\n")
    print("Investment Calculator")
    deposit_amount = float(input("Enter amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    investment_period = int(input("Enter the number of years you plan on investing: "))
    type_interest = input("Enter either 'simple' or 'compound' from the menu above to proceed: ")
    #Checks what type of interest calculation to user would like to carry out
    if type_interest.lower() == 'simple':
        #simple interest is calculated using relevant formula
        simple_amount = deposit_amount * (1 + (interest_rate/100)* years_investing)
        print("The total amount when simple interest is applied is: ", simple_amount)
    elif type_interest.lower() == 'compound':
        #compound interest is calculated using relevant formula
        compound_amount = deposit_amount * math.pow((1 + (interest_rate/100)),years_investing)  
        rounded_amount = round(compound_amount,2) #rounded to 2.d.p  
        print("The total amount when compound interest is applied is: ", rounded_amount)
    else:
        print("Invalid input - restart program")


    #Checks if user input was "bond" and provides corresponding info and performs revelant calculations
elif user_choice.lower() == "bond":
    print("\n")
    print("Bond Calculator")
    present_value_house = float(input("Enter present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    interest_rate = interest_rate/100 #divide interest rate by 100
    months_repay_bond = int(input("Enter the number of months you plan to repay the bond: "))
    monthly_interest = interest_rate / 12
    #Bond repayment is calculated using the relevant formula
    bond_repayment = (monthly_interest * present_value_house) / (1-(1+ monthly_interest) **(-months_repay_bond))
    rounded_repayment = round(bond_repayment,2) #rounded to 2.d.p
    print("Your monthly repayment amount: ",rounded_repayment )

    #output when user enters invalid input
else:
    print("Invalid input - restart program and choose one of the options provided")