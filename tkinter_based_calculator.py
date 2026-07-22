import tkinter as tk


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    box.delete(1.0, "end")
    box.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        box.delete(1.0, "end")
        box.insert(1.0, result)
    except:
        clear_field()
        box.insert(1.0, "Error")

def clear_field():
    global calculation
    box.delete(1.0, "end")
    

root = tk.Tk()

#window code
root.geometry("500x500")
root.title("calculator")

{"UI design code"}

label = tk.Label(root,text = "calculator",font=("Arial",18))
label.pack(padx=20, pady=20)

box = tk.Text(root,height=3, font=('Arial',18))
box.pack(padx =10, pady = 10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)
buttonframe.columnconfigure(5, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18), command = lambda: add_to_calculation(1))
btn1.grid(row=0, column=0, sticky="we")

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18), command = lambda: add_to_calculation(2))
btn2.grid(row=0, column=1, sticky="we")

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18), command = lambda: add_to_calculation(3))
btn3.grid(row=0, column=2, sticky="we")

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18), command = lambda: add_to_calculation(4))
btn4.grid(row=1, column=0, sticky="we")

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18), command = lambda: add_to_calculation(5))
btn5.grid(row=1, column=1, sticky="we")

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18), command = lambda: add_to_calculation(6))
btn6.grid(row=1, column=2, sticky="we")

btn7 = tk.Button(buttonframe, text="7", font=('Arial', 18), command = lambda: add_to_calculation(7))
btn7.grid(row=2, column=0, sticky="we")

btn8 = tk.Button(buttonframe, text="8", font=('Arial', 18), command = lambda: add_to_calculation(8))
btn8.grid(row=2, column=1, sticky="we")

btn9 = tk.Button(buttonframe, text="9", font=('Arial', 18), command = lambda: add_to_calculation(9))
btn9.grid(row=2, column=2, sticky="we")

btn10 = tk.Button(buttonframe, text="0", font=('Arial', 18), command = lambda: add_to_calculation(0))
btn10.grid(row=3, column=0, sticky="we")

btn11 = tk.Button(buttonframe, text="+", font=('Arial', 18), command = lambda: add_to_calculation("+"))
btn11.grid(row=3, column=1, sticky="we")

btn12 = tk.Button(buttonframe, text="-", font=('Arial', 18), command = lambda: add_to_calculation("-"))
btn12.grid(row=3, column=2, sticky="we")

btn13 = tk.Button(buttonframe, text="*", font=('Arial', 18), command = lambda: add_to_calculation("*"))
btn13.grid(row=4, column=0, sticky="we")

btn14 = tk.Button(buttonframe, text="/", font=('Arial', 18), command = lambda: add_to_calculation("/"))
btn14.grid(row=4, column=1, sticky="we")

btn15 = tk.Button(buttonframe, text="=", font=('Arial', 18), command = evaluate_calculation)
btn15.grid(row=4, column=2, sticky="we")

btn16 = tk.Button(buttonframe, text="(", font=('Arial', 18), command = lambda: add_to_calculation("("))
btn16.grid(row=5, column=0, sticky="we")

btn17 = tk.Button(buttonframe, text=")", font=('Arial', 18), command = lambda: add_to_calculation(")"))
btn17.grid(row=5, column=1, sticky="we")

btn18 = tk.Button(buttonframe, text="C", font=('Arial', 18), command = clear_field)
btn18.grid(row=5, column=2, sticky="we")

buttonframe.pack(fill = "x")


root.mainloop()