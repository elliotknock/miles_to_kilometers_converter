from tkinter import *


def miles_to_km():
    user_miles = float(miles_input.get())
    km = round(user_miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equal to
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Answer
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Km
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
