import numpy as np
import matplotlib.pyplot as plt
import control 
import math

# Parametros del PID 
Kp = 2
Ti = 3
Td = -1/3

######################################
# Funcion de transferencia de la planta 
Np = np.array([1])
Dp = np.array([1, -1])
Gp = control.tf(Np, Dp)

print("Funcion de transferencia Gp(s) ", Gp)

# FUNCION DE TRANSFERENCIA DEL PID
alfa0 = Kp
alfa1 = Kp * Ti
alfa2 = Kp * Ti * Td
Npid = np.array([alfa2, alfa1, alfa0])
Dpid = np.array([Ti, 0])
C = control.tf(Npid, Dpid)
print("Control PID, ", C)

######################################
# Funcion de transferencia de la retroalimentacion
N_H = np.array([1])    
D_H = np.array([1])

H = control.tf(N_H, D_H)
print("Funcion de transferencia total", H)

# Funcion de transferencia de trayectoria directa 
# G(s) = C(s) * Gp(s)
G = control.series(C, Gp)

# FUNCION DE TRANSFERENCIA TOTAL
# T(s) = G(s)/(1 + G(s))
T = control.feedback(G, H)

######################################
# POLOS del sistema en lazo cerrado
polos = control.pole(T)
print("Los polos son: ", polos)

ceros = control.zero(T)
print("Ceros: ", ceros) 

# Grafica de los polos y ceros 
control.pzmap(T)
plt.grid()
plt.show()

######################################
# Respuesta del sistema en lazo cerrado
t, y = control.step_response(T)
plt.plot(t, y)
plt.title("Respuesta del control lazo cerrado")
plt.xlabel("Tiempo (t)")
plt.ylabel("y(t)")
plt.grid()
plt.show()