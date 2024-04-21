import tkinter as tk
from tkinter import messagebox
import numpy as np

from lib.calculate_least_squares import calculate_least_squares
from lib.show_graphic import show_graphic

class MainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mínimos Cuadrados")
        
        self.label_x = tk.Label(self, text="Ingrese valores de X separados por espacios:")
        self.label_x.pack()
        self.entry_x = tk.Entry(self, width=50)
        self.entry_x.pack()

        self.label_y = tk.Label(self, text="Ingrese valores de Y separados por espacios:")
        self.label_y.pack()
        self.entry_y = tk.Entry(self, width=50)
        self.entry_y.pack()

        self.button_calculate = tk.Button(self, text="Calcular", command=self.on_calculate_pressed)
        self.button_calculate.pack()

        # self.label_resultado = tk.Label(self, text="")
        # self.label_resultado.pack()

    def on_calculate_pressed(self):
        try:
            x = np.array(list(map(float, self.entry_x.get().split())))
            y = np.array(list(map(float, self.entry_y.get().split())))
            m, c = calculate_least_squares(x, y)
            show_graphic(x, y, m, c)
            # self.label_resultado.config(text=f"Pendiente: {m:.2f}, Intercepto: {c:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

