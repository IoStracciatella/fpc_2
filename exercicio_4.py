# Área entre curvas Pelo Método Monte Carlo

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Definição das funções
def f(x):
    return 1 + 0.5 * np.sin(2*x)**3

def g(x):
    return 3 + 0.5 * np.cos(3*x)**5

# Intervalo de [0, 2π]
a, b = 0, 2 * np.pi

# Gerando valores de x
x = np.linspace(a, b, 1000)

# Plotando as funções f(x) e g(x)
plt.plot(x, f(x), label='f(x) = 1 + 0.5 * sin^3(2x)')
plt.plot(x, g(x), label='g(x) = 3 + 0.5 * cos^5(3x)')
plt.fill_between(x, f(x), g(x), where=(f(x) < g(x)), color='gray', alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico das funções f(x) e g(x)')
plt.legend()
plt.show()

# Calculando a área entre as curvas usando integração numérica
def integrand(x):
    return abs(f(x) - g(x))

area_integral, _ = quad(integrand, a, b)
print(f'Área entre as curvas (integração): {area_integral}')

# Estimando a área com o método de Monte Carlo
N = 100000  # número de pontos
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(min(f(x), g(x)), max(f(x), g(x)), N)

below_curves = np.where((y_rand > f(x_rand)) & (y_rand < g(x_rand)))
area_monte_carlo = (b - a) * (max(f(x)) - min(g(x))) * len(below_curves[0]) / N
print(f'Área entre as curvas (Monte Carlo): {area_monte_carlo}')