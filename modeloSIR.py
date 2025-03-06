import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parâmetros do modelo SIR
def modelo_SIR(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Condições iniciais
N = 1000  # População total
I0 = 1     # Caso inicial infeccioso
S0 = (N - I0) / N  # Fração de suscetíveis inicial
R0 = 0.0  # Fração de recuperados inicial
y0 = [S0, I0/N, R0]  # Condições iniciais em frações

# Parâmetros de simulação
t = np.linspace(0, 100, 1000)   # Tempo (dias)
gamma = 0.1                     # Taxa de recuperação (1/dias)
R0_values = [2.0, 3.0, 4.0]     # Diferentes valores de R₀

# Simulação para cada R₀
plt.figure(figsize=(10, 6))
for R0 in R0_values:
    beta = R0 * gamma
    sol = odeint(modelo_SIR, y0, t, args=(beta, gamma))
    S, I, R = sol.T
    plt.plot(t, I * N, label=f'R₀ = {R0}') 

plt.title('Dinâmica de uma Epidemia - Modelo SIR')
plt.xlabel('Tempo (dias)')
plt.ylabel('Número de Infectados')
plt.legend()
plt.xlim(0, 100)
plt.ylim(0, N)
plt.grid(True)
plt.savefig(f'grafico_modeloSIR.png')
plt.show()