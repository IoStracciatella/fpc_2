# Exercício 4 c/ Parábolas

import numpy as np
import matplotlib.pyplot as plt

# Definindo as funções
def f(x):
    return 1 + 0.5 * np.sin(2*x)**3

def g(x):
    return 3 + 0.5 * np.cos(3*x)**5

# Funções das parábolas
def parabola_esquerda(x):
    return -1.25 * (x - 0)**2 + 1

def parabola_direita(x):
    return -1.25 * (x - 2*np.pi)**2 + 1

# Intervalo de [0, 2π]
a, b = 0, 2 * np.pi

# Gerando valores de x
x = np.linspace(a, b, 1000)

# Plotando as funções f(x), g(x) e as parábolas
plt.plot(x, f(x), label='f(x)')
plt.plot(x, g(x), label='g(x)')
plt.plot(x, parabola_esquerda(x), label='Parábola Esquerda')
plt.plot(x, parabola_direita(x), label='Parábola Direita')
plt.fill_between(x, f(x), g(x), where=(f(x) < g(x)), color='gray', alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Região entre f(x), g(x), e as parábolas')
plt.show()

# Estimando a área com o método de Monte Carlo
N = 100000  # número de pontos aleatórios
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(-1.5, 3.5, N)

# Verificando pontos dentro da área
inside = np.where((y_rand > f(x_rand)) & (y_rand < g(x_rand)) & 
                  (y_rand > parabola_esquerda(x_rand)) & (y_rand < parabola_direita(x_rand)))

# Plotando os pontos
plt.plot(x_rand, y_rand, 'r.', markersize=1, label='Pontos fora')
plt.plot(x_rand[inside], y_rand[inside], 'b.', markersize=1, label='Pontos dentro')
plt.legend()
plt.title('Monte Carlo - Pontos dentro e fora da região')
plt.show()

# Calculando a área
area_monte_carlo = (b - a) * (3.5 + 1.5) * len(inside[0]) / N
print(f'Área estimada (Monte Carlo): {area_monte_carlo}')