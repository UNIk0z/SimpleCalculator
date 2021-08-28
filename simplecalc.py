import tkinter as tk


#Defs for calculation

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#Programs root, geometry of the window and the name
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("355x375")


text_result = tk.Text(root, height=2, width=16, font=("Arial", 30))
text_result.grid(columnspan=5)

#Buttons for the calculations
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=10, font=("Ariel", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=10, font=("Ariel", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=10, font=("Ariel", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=10, font=("Ariel", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=10, font=("Ariel", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=10, font=("Ariel", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=10, font=("Ariel", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=10, font=("Ariel", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=10, font=("Ariel", 14))
btn_9.grid(row=4, column=3)
btn_10 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=10, font=("Ariel", 14))
btn_10.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=10, font=("Ariel", 14))
btn_plus.grid(row=5, column=1)
btn_min = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=10, font=("Ariel", 14))
btn_min.grid(row=5, column=3)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=10, font=("Ariel", 14))
btn_div.grid(row=6, column=1)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=10, font=("Ariel", 14))
btn_mul.grid(row=6, column=2)
btn_op = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=10, font=("Ariel", 14))
btn_op.grid(row=6, column=3)
btn_cl = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=10, font=("Ariel", 14))
btn_cl.grid(row=7, column=1)
btn_eq = tk.Button(root, text="=", command=evaluate_calculation, width=21, font=("Ariel", 14))
btn_eq.grid(row=7, column=2, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_field, width=21, font=("Ariel", 14))
btn_clear.grid(row=8, column=2, columnspan=2)

root.mainloop()
