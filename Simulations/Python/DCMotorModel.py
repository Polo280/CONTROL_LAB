# Simulacion de la dinamica del motor 

###############################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # Integracion numerica
import math
###############################################################
# Parametros del motor (normalmente vienen en las hojas de datos)
Ra = 4.5          # Resistencia de armadura
La = 0.00088      # Inductancia de armadura 
kb = 0.83         # Constante de fuerza electromotriz
km = 0.83         # Constante del motor
Jm = 0.0078       # Momento de inercia del motor 
B = 0.0001        # Friccion del motor 
va = 12           # Voltaje de alimentacion
###############################################################
# Vector de tiempo de simulacion en segundos
start = 0
stop = 0.5
step = 1e-3
t = np.arange(start, stop, step)
###############################################################

# Modelo matematico del motor
def f(x, t):
    Tl = 0.05* np.exp(-5*t)  # Torque de carga
    dx_dt = [0, 0, 0]
    dx_dt[0] = x[1]
    dx_dt[1] = - (B/Jm) * x[1] + (km/Jm) * x[2] - (1/Jm) * Tl
    dx_dt[2] = - (kb/La) * x[1] - (Ra/La) * x[2] + (1/La) * va
    return dx_dt

# Resolucion de las ecuaciones diferenciales
s = odeint(f, y0=[0, 0, 0], t=t)    # Al tener 3 variables de estado necesitamos 3 condiciones iniciales para resolver (posicion angular, vel angular, corriente)
print('Solución', s)

# Grafica posicion angular
plt.plot(t, s[:, 0], 'b', label='Theta')
plt.title("Posicion Angular")
plt.xlabel("t")
plt.ylabel("Theta")
plt.grid()
plt.show()

# Grafica velocidad angular 
plt.plot(t, s[:, 1], 'b', label='Theta')
plt.title("Velocidad Angular")
plt.xlabel("t")
plt.ylabel("w")
plt.grid()
plt.show()

# Grafica corriente
plt.plot(t, s[:, 2], 'b', label='Theta')
plt.title("Corriente")
plt.xlabel("t")
plt.ylabel("Current A")
plt.grid()
plt.show()