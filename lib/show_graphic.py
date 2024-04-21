import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_graphic(x, y, m, c):
        plt.figure(figsize=(6, 4))
        plt.scatter(x, y, color='blue', label='Datos')
        plt.plot(x, m*x + c, 'r', label=f'Y = {m:.2f}X + {c:.2f}')
        plt.title('Gráfico de Regresión Lineal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()