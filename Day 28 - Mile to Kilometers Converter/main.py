import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_entry = tkinter.Entry(window, border="1", borderwidth="2")
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=3)

def calculate():
    try:
        miles = miles_entry.get()
        conversion = float(miles) * 1.6
        kilometer_result_label.config(text=f"{conversion}")
    except ValueError:
        kilometer_result_label.config(text="Invalid Input")

calculate_btn = tkinter.Button(window,text="Calculate", command=calculate)
calculate_btn.grid(row=2, column=1)

window.mainloop()