"""
This week we will implement “if statements” in a program.  Your program will calculate the cost of  fiber optic cable installation by multiplying the number of feet needed by $.87.  We will also evaluate a bulk discount.  You will prompt the user for the number of fiber optic cable they need installed.  Using the default value of $.87 calculate the total expense.  If the user purchases more than 100 feet they are charged $.80 per foot.  If the user purchases more than 250 feet they will be charged $.70 per foot.  If they purchase more than 500 feet they will be charged $.50 per foot.

    Display a welcome message for your program. 
    Get the company name from the user
    Get the number of feet of fiber optic cable to be installed from the user
    Evaluate the total cost based upon the number of feet requested.
    Display the calculated information including the number of feet requested and company name.
"""

# Welcome Message
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


# Customer information requested
def customer_data():
    # waiting for user input
    company_name = input("What is your company name? ")
    while True:
        cable_feet = input("Enter the number of feet to be installed: ")

        # test cable_feet
        try:
            if float(cable_feet): break
        except:
            print("Cable feet was not a number.",
                  " Please enter a valid number")

    return company_name, float(cable_feet)


# determine total cost
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

    # input_length * price = cost
    cost = price*input_length

    return cost, price

welcome()
name, length = customer_data()
tot_cost, install_rate = calc_cost(length)

print("Welcome {}, your installation rate is ${:0.2f}/foot.".format(name, install_rate))
print("Based on your installation length of {:0.2f} feet, your total cost will be: ${:0.2f}.".format(length, tot_cost))
