# File:   DSC510_Assignment_10.py
# Name:   Kevin Paulovici
# Date:   2/17/19
# Course: DSC 510 - Introduction to Programming
# School: Bellevue University
# Desc:   This module is for week 10 programming assignment.

import requests
import tkinter
from tkinter import ttk

# Function: main
#
# Desc: Function defines the best_joke to be displayed as an example / my favorite.
#       This also calls the createGUI function to set things up for the user.
#
def main():
    # define best joke as a global for outer scope use
    global best_joke
    best_joke = "By the way: Chuck Norris doesn't need try-catch, exceptions are too afraid to raise."

    # set the GUI
    masterW = tkinter.Tk()
    createGui(masterW)
    masterW.mainloop()

# Function: getJoke
#
# Desc: Function waits for the user to click the button.
#       If connection is successful the request output is sent to parseJoke.
#       If the connection fails an error message is output.
#
def getJoke():
    global outputLabel  # from createGui()

    # API connection
    link = 'https://api.chucknorris.io/jokes/random'

    # request the joke
    try:
        joke = requests.get(link).json()
        parseJoke(joke)
    except:
        joke = 'Looks like something went wrong with your request'
        outputLabel.config(text=joke)


# Function: parseJoke
#
# Desc: Function parses the joke from getJoke and outputs the result.
#       If the parsing fails there is an issue with the getJoke data
#       and an error message is output.
#
def parseJoke(joke):
    global outputLabel  # from createGui()
    # try to parse the joke dictionary
    try:
        jokeParsed = joke['value']
    except:
        jokeParsed = "Hmmm, this doesn't look like a joke"

    # update the outputLabel
    outputLabel.config(text=jokeParsed)

# Function: welcomeMessage
#
# Desc: Function sets up the header in the gui. Since this is a gui application
#       there is no real reason to welcome the user like a text based application.
#
def welcomeMessage(line):
    name = 'Created by: Kevin Paulovici'
    school = 'For: Bellevue University DSC510'
    project = 'Chuck Norris Random Joke Generator'
    temp = ''

    if line == 0:
        temp = project
    elif line == 1:
        temp = name
    elif line == 2:
        temp = school

    welcome = '{}'.format(temp)

    return welcome


# Function: createGui
#
# Desc: Function sets up the gui.
#
def createGui(master):
    # define outputLabel as global for outer scope
    global outputLabel
    global best_joke  # from main()

    # set basic gui features
    master.title('Chuck Norris Joke Generator')
    master.geometry('500x350+600+400')
    master.resizable(False, False)

    # set welcome frame/message
    welcomeFrame = tkinter.Frame(master).pack()

    for i in range(3):
        welcome = welcomeMessage(i)
        tkinter.Label(welcomeFrame, text=welcome,  bg='light blue',
                      font=('Times New Roman', 12)).pack(padx=10, fill='x')

    # main frame for input/out
    mainFrame = tkinter.Frame(master).pack()

    tkinter.Label(mainFrame, text='Click the button to get a random Chuck Norris '
                                             'joke...',
                             font=('Times New Roman', 14, 'bold')).pack(padx=10, pady=10)

    ttk.tkinter.Button(mainFrame, text='Joke Generator', font=('Times New Roman', 20, 'bold'),
                       background='red', command=getJoke).pack()

    # output label
    tkinter.Label(mainFrame, text='Your random joke:', font=('Times New Roman', 12)).pack(anchor='w', padx=10)
    test = 'You need to click the button!'
    outputLabel = tkinter.Label(mainFrame, text=test, wraplength=400, justify=tkinter.LEFT,
                                font=('Times New Roman', 12))
    outputLabel.pack(anchor='w', padx=10, pady=5, fill='x')

    tkinter.Label(mainFrame, text=best_joke, font=('Times New Roman', 10)).pack(anchor='w', padx=10, side='bottom')


# run the program
if __name__ == '__main__':
    main()
