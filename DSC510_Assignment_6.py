# File:   DSC510_Assignment_6.py
# Name:   Kevin Paulovici
# Date:   1/19/19
# Course: DSC 510 - Introduction to Programming
# School: Bellevue University
# Desc:   This module is for week 6 programming assignment.
#completes: 1

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
    ##      Welcome to Week 6                ##
    ##                                       ##
    ##      For and While Loops              ##
    ##                                       ##
    ##   This program will perform various   ##
    ##   calculations (addition, subtraction,##
    ##   multiplication, division, and       ##
    ##   average calculation)                ##
    ##                                       ##
    ###########################################
    """)

# Function: main
#
# Parameter:
#   In:     none
#   Out:    none
# Returns:  none
#
# Desc:     The main function runs until the user terminates the program.
#           The user is prompted to enter an operation for performCalculation.
#           The main function will validate the entered operation.
#           The main function will call other functions.
# completes: 4
def main():
    welcome()
    while True:
        print("\n Welcome to the main function.\n\n",
              "Only a value of 0 will terminate this program,\n",
              "otherwise enter anything: \n")

        user = input(" Enter 0 or anything: ")

        if user == "0": break

        # get operation to perform
        while True:
            operation = input(" Enter an operation to occur, "
                              "valid operation are: + - * /: ")

            if operation == "+" or operation == "-" \
                    or operation == "*" or operation == "/":
                performCalculation(operation)
                break
            else:
                print(" The {} operation is not valid!".format(operation))

        calculateAverage()

    print(" End of program, thanks for playing!")

# Function: performCalculation
#
# Parameter:
#   In:     op - user supplied math operation
#   Out:    none
# Returns:  none
#
# Desc:     This function takes a user supplied operation. The
#           operation will be performed on two user supplied values
#           and print the result.
# completes: 2
def performCalculation(op):
    op_calc = ""  # hold for calculated value
    print("\n Welcome to the performAverage function.\n\n"
          " Enter numbers to perform {} operation one at a time."
          .format(op))

    # Get the numbers to be averaged
    nums = getNumbers()

    if op == "+":
        op_calc = nums[0] + nums[1]
    elif op == "-":
        op_calc = nums[0] - nums[1]
    elif op == "*":
        op_calc = nums[0] * nums[1]
    elif op == "/":
        try:
            op_calc = nums[0] / nums[1]

        except:
            op_calc = "N/A"
            print(" The following operation cannot occur: "
                  "{} {} {}\n".format(nums[0], op, nums[1]))

    print("\n The numbers entered were: {}\n"
          " The operation entered was: {}\n"
          " The calculation of {} {} {} is: {}\n"
          .format(nums, op, nums[0], op, nums[1], op_calc))

# Function: calculateAverage
#
# Parameter:
#   In:     none
#   Out:    none
# Returns:  none
#
# Desc:     This function asks the user how many numbers they
#           want to input. The user enters those numbers
#           through getNumbers. The total and average
#           numbers will be calculated and printed.
# completes: 3

def calculateAverage():
    print(" Welcome to the calculateAverage function.\n")
    count_num = []  # hold for user input
    total = 0    # hold for calc
    average = 0  # hold for calc

    # Get how many numbers to enter
    while True:
        try:
            count = float(input(" How many numbers do you want to use ( > 0): "))
        except:
            print(" That is not a valid number.")
            continue

        try:
            if float(count) and float(count) > 0:
                count_num.append(float(count))
                break
            else:
                print(" Enter a valid number! (> 0)")
                continue
        except:
            print(" Enter a valid number! (> 0)")

    # Get the numbers to be averaged
    nums = getNumbers(*count_num)

    for num in nums:
        total += num
        average = total / len(nums)

    print("\n The numbers entered were: {}\n"
          " The total is: {}\n"
          " The average is: {}".format(nums, total, average))

# Function: getNumbers
#
# Parameter:
#   In:     *count_num - optional input
#   Out:    none
# Returns:  numbers - list of user input numbers
#
# Desc:     This function asks the user for values to
#           to be added to a list which get used for
#           various calculations.
def getNumbers(*args):
    numbers = []
    user_input = 2  # default to 2 for performCalculation
    if args:        # for calculateAverage
        user_input = args[0]

    while len(numbers) < user_input:
        temp = input(" Enter number: ")
        try:
            if float(temp) or temp == "0" or temp == "0.0":
                numbers.append(float(temp))
        except:
            print(" ", temp, "is not valid!")

    return numbers

# RUN THE PROGRAM
main()
