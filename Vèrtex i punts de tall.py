from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def calcular_y_graficar():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    if a == 0:
        messagebox.showerror(":(", "El valor de 'a' no pot ser 0 (no seria una paràbola).")

    if a != 0:

        # Càlcul del vèrtex
        x = -b / (2 * a)
        y= a * x**2 + b * x + c

        # Assenyalar el vèrtex
        label_resultat.configure(text=f"Vèrtex: ({x:.2f}, {y:.2f})")

        # Graficar
        domini = np.linspace(x - 50, x + 50, 400)
        recorregut = a * domini**2 + b * domini + c

        plt.figure(figsize=(6, 4))
        plt.plot(domini, recorregut, label="Paràbola", color='#FF81C0')
        plt.plot(x, y, 'o', color='turquoise', label="Vèrtex")
        plt.title("Gràfica de la funció quadràtica", color='#FF81C0')
        plt.xlabel("x", color='pink')
        plt.ylabel("y", color='pink')
        plt.grid(True)
        plt.legend()
        plt.axhline(0, color='pink', linewidth=1)
        plt.axvline(0, color='pink', linewidth=1)
        plt.show()


# Finestra de tkinter
Finestra = Tk()
Finestra.title("Calculadora del vèrtex d'una paràbola")
Finestra.geometry("450x150")
Finestra.config(bg="pink")

Valor_a=Label(text="a:")
Valor_a.grid(row=0, column=0)

entry_a = Entry(width=60)
entry_a.grid(row=0, column=1)

Valor_b=Label(text="b:")
Valor_b.grid(row=1, column=0)

entry_b = Entry(width=60)
entry_b.grid(row=1, column=1)

Valor_c=Label(text="c:")
Valor_c.grid(row=2, column=0)

entry_c = Entry(width=60)
entry_c.grid(row=2, column=1)

botóbruh= Button(text="Calcular y Graficar", command=calcular_y_graficar)
botóbruh.grid(row=3, column=0, columnspan=2, pady=10)

label_resultat = Label(text="Vèrtex: ")
label_resultat.grid(row=4, column=0, columnspan=2)


Finestra.mainloop()



