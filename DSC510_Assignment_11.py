# File:   DSC510_Assignment_11.py
# Name:   Kevin Paulovici
# Date:   2/23/19
# Course: DSC 510 - Introduction to Programming
# School: Bellevue University
# Desc:   This module is for week 11 programming assignment.

import tkinter
import locale


# Function: main
#
# Desc: Function defines the locale and sets up the GUI to interact with the user.
#
def main():
    locale.setlocale(locale.LC_ALL, '')

    # set the GUI
    masterWindow = tkinter.Tk()
    CreateGui(masterWindow)
    masterWindow.mainloop()


# Function: welcomeMessage
#
# Desc: Function sets up the welcome message and directions for the user.
#
def welcomeMessage():
    line1 = 'Welcome to The Python Diner!\n'
    line2 = 'Select your items and they will be added to your cart.\n'
    line3 = 'You can always start over by by clearing your items.\n'

    welcome = '{} {} {}'.format(line1, line2, line3)

    return welcome


# Function: banner
#
# Desc: Function sets up the header banner.
#
def banner(line):
    name = 'Created by: Kevin Paulovici'
    school = 'For: Bellevue University DSC510'
    project = 'Cash Register Program'
    temp = ''

    if line == 0:
        temp = project
    elif line == 1:
        temp = name
    elif line == 2:
        temp = school

    welcome = '{}'.format(temp)

    return welcome


# Class: CashRegister
#
# Desc: CashRegister class keeps track of item count and price that the user selects.
#       An instance of CashRegister is created in CreateGui and accessed by GUI features.
#
class CashRegister:
    price = 0           # initial price of item
    totalPrice = 0      # initial total price of all items
    itemCount = 0       # initial count of items

    def addItem(self, price):
        self.price = price
        self.itemCount += 1
        self.totalPrice += self.price

    @property
    def getTotal(self):
        return self.totalPrice

    @property
    def getCount(self):
        return self.itemCount


# Class: CreateGui
#
# Desc: CreateGui is a class for the GUI to interact with the user.
#       An instance of CashRegister is created here to track user selections.
#
class CreateGui:

    # set up instance of CashRegister
    startCalc = CashRegister()

    # set up class variables
    menu = [{'1.50': 'Egg and spam'},
            {'1.90': 'Egg, bacon and spam'},
            {'2.20': 'Egg, bacon, sausage and spam'},
            {'2.50': 'Spam, bacon, sausage and spam'},
            {'2.60': 'Spam, egg, spam, spam, bacon and spam'},
            {'2.90': 'Spam, sausage, spam, spam, spam, bacon, spam, tomato and spam'},
            {'2.70': 'Spam, spam, spam, egg and spam'},
            {'3.50': 'Spam, spam, spam, spam, spam, spam, baked beans, spam'},
            {'2.25': 'Spam, spam and spam'},
            {'9.99': """Lobster thermidor aux crevettes with a mornay sauce served in 
             provencale manner with shallots and aubergines, garnished with
             truffle pate, brandy and with a fried egg on top and spam"""}]

    outputMessage = 'You need to select and item to add to your cart...'
    outputCount = '0'
    outputTotal = '$ 0.00'

    # method to access button selection
    def userAddItem(self):
        # pass buttonPrice to CashRegister instance
        self.startCalc = CreateGui.startCalc
        self.startCalc.addItem(float(self.buttonPrice.get()))

        # update output labels
        self.outputUpdate()

    # method to update labels
    def outputUpdate(self):
        # get data for labels
        textUpdate = 'You added 1 item for ${:.02f}'.format(float(self.buttonPrice.get()))
        priceUpdate = locale.currency(float(self.startCalc.getTotal))

        # set the labels
        self.outputLabelVar.set(textUpdate)
        self.totalItemsLabelVar.set(self.startCalc.getCount)
        self.totalPriceLabelVar.set(priceUpdate)

    # method to start a new instance of the CashRegister class
    def startOver(self):
        CreateGui.startCalc = CashRegister()

        # reset output labels and default button selection
        self.buttonPrice.set(1.50)
        self.outputLabelVar.set(CreateGui.outputMessage)
        self.totalItemsLabelVar.set(CreateGui.outputCount)
        self.totalPriceLabelVar.set(CreateGui.outputTotal)

    # initialize the GUI from the main function
    def __init__(self, master):

        # ------------------ set basic gui features -------------------------------------------
        self.master = master
        self.master.title('Cash Register Program - Python Diner')
        self.master.geometry('500x700+600+400')
        self.master.resizable(False, False)

        # ------------------ add gui widgets        -------------------------------------------

        # set banner frame and banner widgets
        self.bannerFrame = tkinter.Frame(master).pack()

        for i in range(3):
            self.banner = banner(i)
            tkinter.Label(self.bannerFrame, text=self.banner, bg='light blue',
                          font=('Times New Roman', 12)).pack(padx=10, fill='x')

        # set the main frame
        self.mainFrame = tkinter.Frame(master).pack()

        # set the welcome message
        self.welcome = tkinter.Label(self.mainFrame, text=welcomeMessage(),
                                     font=('Times New Roman', 14, 'bold')).pack(padx=10, pady=5)

        # set the items to add to cart
        tkinter.Label(self.mainFrame, text='Select your item to add:',
                      font=('Times New Roman', 12)).pack(anchor='w', padx=10)

        # set the button selections
        self.buttonPrice = tkinter.StringVar()
        self.buttonPrice.set(1.50)

        for self.m in CreateGui.menu:
            for self.price, self.mDes in self.m.items():
                # radio buttons for menu items
                tkinter.Radiobutton(self.mainFrame, text=self.mDes, variable=self.buttonPrice,
                                    command=self.userAddItem, value=float(self.price),
                                    justify=tkinter.LEFT,
                                    font=('Times New Roman', 12)).pack(anchor='w', padx=10, pady=1)

        # set the output
        self.outputLabelVar = tkinter.StringVar()
        self.outputLabelVar.set(CreateGui.outputMessage)
        self.outputLabel = tkinter.Label(self.mainFrame, textvariable=self.outputLabelVar,
                                         font=('Times New Roman', 12, 'bold')).pack(padx=10, pady=10)

        tkinter.Button(self.mainFrame, text='Clear Items', command=self.startOver,
                       height=2, width=30, bg='red').pack(padx=10, pady=5)

        tkinter.Label(self.mainFrame, text='Total Items: ',
                      font=('Times New Roman', 14, 'bold')).pack(side=tkinter.LEFT, padx=40)

        self.totalItemsLabelVar = tkinter.StringVar()
        self.totalItemsLabelVar.set(CreateGui.outputCount)
        self.totalItemsLabel = tkinter.Label(self.mainFrame, textvariable=self.totalItemsLabelVar,
                                             font=('Times New Roman', 14)).pack(side=tkinter.LEFT)

        tkinter.Label(self.mainFrame, text='Total Price: ',
                      font=('Times New Roman', 14, 'bold')).pack(side=tkinter.LEFT, padx=30, fill=tkinter.X)

        self.totalPriceLabelVar = tkinter.StringVar()
        self.totalPriceLabelVar.set(CreateGui.outputTotal)
        self.totalPriceLabel = tkinter.Label(self.mainFrame, textvariable=self.totalPriceLabelVar,
                                             font=('Times New Roman', 14)).pack(side=tkinter.LEFT)


# run the program
if __name__ == '__main__':
    main()
