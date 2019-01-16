# File:   DSC510_Assignment_5.py
# Name:   Kevin Paulovici
# Date:   1/12/19
# Course: DSC 510 - Introduction to Programming
# School: Bellevue University
# Desc:   This module is for week 5 programming assignment.
#
# This week we will modify our If Statement program to add a function to do the heavy lifting.
# Modify your IF Statement program in to add a function. This function will perform the cost calculation.
# The function will have two parameters (feet and price).
# When you call the function, you will pass two arguments to the function; feet of fiber
# to be installed and the cost (remember that price is dependent on the number of feet being installed).
# You probably should have the following:
# 1. Your program must have a header. Use the programing style guide for guidance.
# 2. A welcome message
# 3. A function with two parameters
# 4. A call to the function
# 5. The application should calculate the cost based upon the number of feet being ordered
# 6. A printed message displaying the company name and the total calculated cost

# Function: main
#
# Parameter:
#   In:     none
#   Out:    none
# Returns:  none
#
# Desc:     main block of code to be executed
def main():
    welcome()
    name, feet = customer_data()
    tot_cost, install_rate = calc_cost(feet)
    print_date(name, install_rate, feet, tot_cost)

# Function: welcome
#
# Parameter:
#   In:     none
#   Out:    none
# Returns:  none
#
# Desc:     simple function to welcome the user (customer)
def welcome():
    print("""
    ###########################################
    ##                                       ##
    ##   Welcome to Fiber Optic Installs     ##
    ##                                       ##
    ##   We offer the following rates:       ##
    ##   $0.87/foot                          ##
    ##   $0.80/foot for 100 feet or more     ##
    ##   $0.70/foot for 250 feet or more     ## 
    ##   $0.50/foot for 500 feet or more     ##
    ##                                       ##
    ###########################################
    """)

# Function: print_data
#
# Parameter:
#   In:     name, install_rate, feet, tot_cost
#   Out:    none
# Returns:  none
#
# Desc:     print statements to the user
def print_date(name, install_rate, feet, tot_cost):
    print("Welcome {}, your installation rate is ${:0.2f}/foot."
          .format(name, install_rate))
    print("Based on your installation length of {:0.2f}ft, your total cost"
          " will be: ${:0.2f}.".format(feet, tot_cost))

# Function: customer_data
#
# Parameter:
#   In:     none
#   Out:    none
# Returns:  company_name - company input from customer
#           cable_feet - customer input of cable length (ft)
#
# Desc: Customer information requested
def customer_data():
    # waiting for user input
    company_name = input("What is your company name? ")
    while True:
        cable_feet = input("Enter the number of feet to be installed: ")

        # test cable_feet
        try:
            if float(cable_feet) > 0: break
            elif float(cable_feet) < 0:
                print("Length was not positive, converting to positive")
                break
        except:
            print("Cable feet was not a number.",
                  " Please enter a valid number")

    return company_name, abs(float(cable_feet))

# Function: calc_cost
#
# Parameter:
#   In:     input_length - supplied by customer
#   Out:    none
# Returns:  cost - input_length * price
#           price - determined based on length
#
# Desc:     determine cost and price
def calc_cost(input_length):
    # set price based on length
    if input_length < 100:
        price = 0.87
    elif input_length < 250:
        price = 0.80
    elif input_length < 500:
        price = 0.70
    else:
        price = 0.50

    cost = price*input_length

    return cost, price

main()
