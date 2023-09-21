from tkinter import *


def miles_to_km():
    input_miles = float(input_box.get())
    output_km = input_miles * 1.609
    converted_km.config(text=str(output_km))


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=50, pady=20)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)

miles = Label(text='Miles')
miles.grid(column=2, row=0)

equal = Label(text='is equal to')
equal.grid(column=0, row=1)

converted_km = Label(text='0')
converted_km.grid(column=1, row=1)

km = Label(text='Km')
km.grid(column=2, row=1)

calculate = Button(text='Calculate', command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
