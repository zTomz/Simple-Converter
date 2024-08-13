import tkinter
from tkinter import ttk
from turtle import width

class main:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('400x150')
        self.window.maxsize(width=600, height=150)
        self.window.minsize(width=270, height=150)
        self.window.title('Converter')
        self.window.call('wm', 'iconphoto', self.window._w, tkinter.PhotoImage(file='icon.png'))

        self.title = ttk.Label(self.window, text='Converter', font=("Helvetica", "20", "bold"))
        self.title.place(x=20, y=10, anchor='nw')

        self.degreeInput = tkinter.Text(self.window, width=15, height=1)
        self.degreeInput.place(x=20, y=50, anchor='nw')

        self.selectionBox = tkinter.Listbox(self.window, height=3)
        self.selectionBox.insert(1, 'Celsius -> Fahrenheit')
        self.selectionBox.insert(2, 'Celsius -> Kelvin')
        self.selectionBox.insert(3, 'Fahrenheit -> Celsius')
        self.selectionBox.insert(4, 'Fahreheit -> Kelvin')
        self.selectionBox.insert(5, 'Kelvin -> Celsius')
        self.selectionBox.insert(6, 'Kelvin -> Fahrenheit')
        self.selectionBox.place(x=20, y=80, anchor='nw')

        self.convertButton = ttk.Button(self.window, text='convert', width=15, command=self.getConvertion)
        self.convertButton.place(x=150, y=47.5, anchor='nw')

        self.resultLabel = ttk.Label(self.window, background='grey')

        self.window.mainloop()

    def getConvertion(self):
        try:
            if self.selectionBox.selection_get() == 'Celsius -> Fahrenheit':
                self.celsiusToFahrenheit()
            elif self.selectionBox.selection_get() == 'Celsius -> Kelvin':
                self.celsiusToKelvin()
            elif self.selectionBox.selection_get() == 'Fahrenheit -> Celsius':
                self.fahrenheitToCelsius()
            elif self.selectionBox.selection_get() == 'Fahreheit -> Kelvin':
                self.fahrenheitToKelvin()
            elif self.selectionBox.selection_get() == 'Kelvin -> Celsius':
                self.kelvinToCelsius()
            elif self.selectionBox.selection_get() == 'Kelvin -> Fahrenheit':
                self.kevlinToFahreheit()
        except:
            self.resultLabel.configure(text="A value is missing!", foreground='red')
            self.resultLabel.place(x=150, y=80, anchor='nw')

    def celsiusToFahrenheit(self):
        degree = self.degreeInput.get('1.0', 'end')
        # Float convertierung
        degree = degree.replace(',', '.')
        degree = float(degree)
        # Convertion
        result = degree * 1.8 + 32
        # Output
        self.resultLabel.configure(text=f'{degree} C° in Fahrenheit: {result} F°', foreground='black')
        self.resultLabel.place(x=150, y=80, anchor='nw')

    def celsiusToKelvin(self):
        degree = self.degreeInput.get('1.0', 'end')
        # Float convertierung
        degree = degree.replace(',', '.')
        degree = float(degree)
        # Convertion
        result = degree + 273.15
        # Output
        self.resultLabel.configure(text=f'{degree} C° in Kelvin: {result} K', foreground='black')
        self.resultLabel.place(x=150, y=80, anchor='nw')

    def fahrenheitToCelsius(self):
        degree = self.degreeInput.get('1.0', 'end')
        # Float convertierung
        degree = degree.replace(',', '.')
        degree = float(degree)
        # Convertion
        result = (degree - 32) / 1.8
        # Output
        self.resultLabel.configure(text=f'{degree} F° in Celsius: {result} C°', foreground='black')
        self.resultLabel.place(x=150, y=80, anchor='nw')

    def fahrenheitToKelvin(self):
        degree = self.degreeInput.get('1.0', 'end')
        # Float convertierung
        degree = degree.replace(',', '.')
        degree = float(degree)
        # Convertion
        result = (degree + 459.67) / 1.8
        # Output
        self.resultLabel.configure(text=f'{degree} F° in Kelvin: {result} K', foreground='black')
        self.resultLabel.place(x=150, y=80, anchor='nw')

    def kelvinToCelsius(self):
        degree = self.degreeInput.get('1.0', 'end')
        # Float convertierung
        degree = degree.replace(',', '.')
        degree = float(degree)
        # Convertion
        result = degree - 273.15
        # Output
        self.resultLabel.configure(text=f'{degree} K in Celsius: {result} C°', foreground='black')
        self.resultLabel.place(x=150, y=80, anchor='nw')

    def kevlinToFahreheit(self):
        degree = self.degreeInput.get('1.0', 'end')
        # Float convertierung
        degree = degree.replace(',', '.')
        degree = float(degree)
        # Convertion
        result = degree * 1.8 - 459.67
        # Output
        self.resultLabel.configure(text=f'{degree} K in Fahreheit: {result} F°', foreground='black')
        self.resultLabel.place(x=150, y=80, anchor='nw')
    
app = main()