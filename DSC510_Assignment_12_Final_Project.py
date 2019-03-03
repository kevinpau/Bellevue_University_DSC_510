# File:   DSC510_Assignment_12_Final_Project.py
# Name:   Kevin Paulovici
# Date:   3/2/19
# Course: DSC 510 - Introduction to Programming
# School: Bellevue University
# Desc:   This module is for the final project assignment.

import tkinter
import requests


# Function: main
#
# Desc: Function sets up the GUI to interact with the user.
def main():
    masterWindow = tkinter.Tk()
    CreateGui(masterWindow)
    masterWindow.mainloop()


# Function: welcomeMessage
#
# Desc: Function sets the welcome message for the user.
def welcomeMessage():
    line1 = ' Welcome to the weather lookup app.\n'
    line2 = 'Start by selecting the zip or city option.\n'
    line3 = 'Then enter the US city or zip you want to lookup.'
    message = '{} {} {}'.format(line1, line2, line3)

    return message


# Class: WeatherRequest
#
# Desc: Class has various methods to set and request data from the openweathermap API.
class WeatherRequest:
    # ------------------  set class variables   -------------------------------------------
    # main variables to be accessed
    data = ''
    valid = False
    url = ''
    APIKEY = '&appid=bd65d0397fc4cce03835ca7560baa443'
    unit = 'imperial'
    country = 'US'
    zipCity = ''
    zipFormat = 'http://api.openweathermap.org/data/2.5/weather?zip='
    cityFormat = 'http://api.openweathermap.org/data/2.5/weather?q='

    # error messages to be sent to CreateGui
    badInputResult = 'N/A'
    badInputErrorMessageZip = "Zip code should be 5 numbers in the format of #####!"
    badInputErrorMessageCity = 'City should not be empty!'
    error_on_connect = 'Sorry, your connection to the openweathermap failed!'

    # initialize the class with the class variables, sets zip/city and input from user (CreateGui --> submit)
    def __init__(self, searchOption, input):
        # initialized main values
        self.data = WeatherRequest.data
        self.valid = WeatherRequest.valid
        self.url = WeatherRequest.url
        self.api = WeatherRequest.APIKEY
        self.units = WeatherRequest.unit
        self.countryInput = WeatherRequest.country
        self.zipCity = WeatherRequest.zipCity
        self.userSearchOption = searchOption
        self.userInput = input

        # error messages
        self.badInputResult = WeatherRequest.badInputResult
        self.badInputErrorMessage = WeatherRequest.badInputErrorMessageZip
        self.badInputErrorMessage = WeatherRequest.badInputErrorMessageCity
        self.error_on_connect = WeatherRequest.error_on_connect

    # Method: checkValidInput
    #
    # Desc: Method checks the user input validity, specifically the zip.
    #       Returns a true/false flag to determine what actions/output to display
    @property
    def checkValidInput(self):
        if self.userSearchOption == 0:  # zip
            if len(self.userInput) == 5 and self.userInput.isnumeric():
                self.valid = True
            else:
                self.valid = False
        elif self.userSearchOption == 1:  # city
            if len(self.userInput) > 0:
                self.valid = True
            else:
                self.valid = False

        return self.valid

    # Method: badInput
    #
    # Desc: Method runs when checkValidInput is false.
    #       Returns a zip/city message for output to display
    @property
    def badInput(self):
        if self.userSearchOption == 0:
            return self.badInputResult, self.badInputErrorMessageZip
        else:
            return self.badInputResult, self.badInputErrorMessageCity

    # Method: getFormat
    #
    # Desc: Method runs when getWeatherData is run.
    #       Sets the url for the request based on zip/city option
    @property
    def getFormat(self):
        if self.userSearchOption == 0:
            self.zipCity = self.zipFormat
        else:
            self.zipCity = self.cityFormat
        self.url = '{}{},{}{}&units={}'.format(self.zipCity, self.userInput, self.countryInput, self.api, self.unit)

        return self.url

    # Method: getWeatherData
    #
    # Desc: Method runs the url from getFormat.
    #       Try's to request data and parse it (parseWeatherData)
    #       If the API cannot connect will return an error message
    #       Results are sent back to CreateGui --> submit to determine what output to display
    def getWeatherData(self):
        try:
            self.data = requests.get(self.getFormat).json()
            dataParse = self.parseWeatherData
            return dataParse
        except:
            return self.badInputResult, self.error_on_connect

    # Method: parseWeatherData
    #
    # Desc: Method try's to parse the data from request.
    #       If successful the name, description, and temps will be set
    #       If those values are unavailable an error occurred and will return the error message
    @property
    def parseWeatherData(self):
        parsedResults = []
        try:
            parsedResults.append(self.data['name'])
            parsedResults.append(self.data['weather'][0]['description'])
            parsedResults.append(int(self.data['main']['temp']))
            parsedResults.append(int(self.data['main']['temp_max']))
            parsedResults.append(int(self.data['main']['temp_min']))
        except:
            if self.data['cod']:
                parsedResults.append(self.data['message'])

        return parsedResults


# class: CreateGui
#
# Desc: Class creates the gui and has various methods to interact with WeatherRequest and set output.
class CreateGui:
    # ------------------  set class variables   -------------------------------------------
    # output tuple with label name and row position - for less repetitive code
    outputNames = [('Current Weather for:', 4), ('Weather Description:', 5),
                   ('Current Temperature:', 6), ('Max Temperature:', 7), ('Min Temperature:', 8)]

    outputMessage = 'You need to run the App...'

    # Method: submit
    #
    # Desc: Main method that is activated by the 'Get Weather Data' button.
    #       Method initializes the WeatherRequest class and pass the zip/city option and user input.
    #       Checks the user input validity, determines what actions to take next.
    #       Output messages and results are set based on the logic set here
    def submit(self):
        # initialize WeatherRequest with zip/city option and user input
        requestWeather = WeatherRequest(self.searchOptionSelection.get(), self.userEntryVal.get())
        if requestWeather.checkValidInput:
            try:
                returnedResults = requestWeather.getWeatherData()
                if len(returnedResults) > 1:
                    self.updateGoodInput(returnedResults)
                else:
                    self.updateBadInputOutput(returnedResults)
            except:
                badInputResults, error_on_connect = requestWeather.getWeatherData()
                self.updateBadInputOutput(error_on_connect, badInputResults)

        else:
            val, mes = requestWeather.badInput
            self.updateBadInputOutput(mes, val)

    # Method: updateGoodInput
    #
    # Desc: If the WeatherRequest was successful with expected data the results are updated.
    def updateGoodInput(self, results):
        # set the results output labels
        self.cityVal.set(results[0])
        self.descriptionVal.set(results[1])
        self.curTempVal.set(str(results[2]) + ' deg. F')
        self.maxTempVal.set(str(results[3]) + ' deg. F')
        self.minTempVal.set(str(results[4]) + ' deg. F')

        self.outputMessageDefault.set('Successfully grabbed data')

    # Method: updateBadInputOutput
    #
    # Desc: If the WeatherRequest failed the results are updated as such.
    #       Various failure methods are captured here. (e.g., bad connection, city not found, no input, bad zip)
    def updateBadInputOutput(self, message, value='N/A'):
        self.cityVal.set(value)
        self.descriptionVal.set(value)
        self.curTempVal.set(value)
        self.maxTempVal.set(value)
        self.minTempVal.set(value)

        # set output error message & reset the entry
        if len(message) > 1:
            self.outputMessageDefault.set(message)
        else:
            self.outputMessageDefault.set(message[0])  # parsed error messages are contained in a list
        self.userEntryVal.set('')

    # Method: clearForm
    #
    # Desc: Resets the form.
    def clearForm(self):
        clear = ''
        self.userEntryVal.set(clear)

        # set the results output labels
        self.cityVal.set(clear)
        self.descriptionVal.set(clear)
        self.curTempVal.set(clear)
        self.maxTempVal.set(clear)
        self.minTempVal.set(clear)

        self.outputMessageDefault.set(CreateGui.outputMessage)

    # initializes the gui and set the widgets
    def __init__(self, master):
        # ------------------ set basic gui features -------------------------------------------
        self.master = master
        self.master.title('Weather App - DSC510 Final')

        # set the window size and location
        self.width = 360
        self.height = 470
        self.screenW = self.master.winfo_screenwidth()
        self.screenH = self.master.winfo_screenheight()
        self.x_coor = (self.screenW/2) - (self.width/2)
        self.y_coor = (self.screenH/2) - (self.height/2)
        self.master.geometry('{}x{}+{:.0f}+{:.0f}'.format(self.width, self.height, self.x_coor, self.y_coor))
        self.master.resizable(False, False)

        # ------------------ add gui widgets        -------------------------------------------

        # set the welcome message
        tkinter.Label(self.master, text=welcomeMessage(),
                      font=('Arial', 12)).grid(row=0, sticky='w', padx=10, pady=10, columnspan=2)

        # set the zip or city labels and buttons
        tkinter.Label(self.master, text='Search option:', font=('Arial', 12)).grid(
            row=1, sticky='e', padx=10, pady=10)

        # set the button selection
        self.searchOptionSelection = tkinter.IntVar()
        self.searchOptionSelection.set(0)

        tkinter.Radiobutton(self.master, text='Zip', variable=self.searchOptionSelection,
                            value=0, justify=tkinter.LEFT,
                            font=('Arial', 12)).grid(row=1, column=1, sticky='w', padx=10, pady=10)

        tkinter.Radiobutton(self.master, text='City', variable=self.searchOptionSelection,
                            value=1, justify=tkinter.LEFT,
                            font=('Arial', 12)).grid(row=1, column=1, sticky='e', padx=10, pady=10)

        # set the entry label and entry space
        tkinter.Label(self.master, text='(US) Zip or City:', font=('Arial', 12)).grid(
            row=2, sticky='e', padx=10, pady=10)

        self.userEntryVal = tkinter.StringVar()
        self.userEntryVal.set('')

        self.userEntry = tkinter.Entry(self.master, textvariable=self.userEntryVal).grid(
            row=2, column=1, ipady=3, sticky='ew', padx=10, pady=10)

        # set the submit and clear buttons
        self.userSubmitButton = tkinter.Button(self.master, text='Get Weather Data',
                                               command=self.submit, font=('Arial', 12)).grid(
            row=3, column=1, sticky='ew', padx=10, pady=10)

        self.clearDataButton = tkinter.Button(self.master, text='Clear Form',
                                              command=self.clearForm, font=('Arial', 12)).grid(
            row=3, column=0, sticky='e', padx=5, pady=10)

        # set the result labels from the class variable outputNames
        for item in CreateGui.outputNames:
            tkinter.Label(self.master, text=item[0], font=('Arial', 12)).grid(
                row=item[1], sticky='e', padx=10, pady=5)

        # set the result output labels
        self.cityVal = tkinter.StringVar()
        self.descriptionVal = tkinter.StringVar()
        self.curTempVal = tkinter.StringVar()
        self.maxTempVal = tkinter.StringVar()
        self.minTempVal = tkinter.StringVar()
        self.cityVal.set('')
        self.descriptionVal.set('')
        self.curTempVal.set('')
        self.maxTempVal.set('')
        self.minTempVal.set('')

        self.city = tkinter.Label(self.master, textvariable=self.cityVal, font=('Arial', 12)).grid(
            row=4, column=1, sticky='w', padx=10, pady=5)

        self.description = tkinter.Label(self.master, textvariable=self.descriptionVal, font=('Arial', 12)).grid(
            row=5, column=1, sticky='w', padx=10, pady=5)

        self.curTemp = tkinter.Label(self.master, textvariable=self.curTempVal, font=('Arial', 12)).grid(
            row=6, column=1, sticky='w', padx=10, pady=5)

        self.maxTemp = tkinter.Label(self.master, textvariable=self.maxTempVal, font=('Arial', 12)).grid(
            row=7, column=1, sticky='w', padx=10, pady=5)

        self.minTemp = tkinter.Label(self.master, textvariable=self.minTempVal, font=('Arial', 12)).grid(
            row=8, column=1, sticky='w', padx=10, pady=5)

        # set output message (errors)
        self.outputMessageDefault = tkinter.StringVar()
        self.outputMessageDefault.set(CreateGui.outputMessage)

        self.outputMessageLabel = tkinter.Label(self.master, textvariable=self.outputMessageDefault,
                                                font=('Arial', 12), wraplength=320)
        self.outputMessageLabel.grid(row=9, columnspan=3, sticky='ew', padx=10, pady=10)


# run the program
if __name__ == '__main__':
    main()
