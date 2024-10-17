import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. Definindo as funções f(x) e g(x)
x_vals = np.linspace(0, 2 * np.pi, 400)
f = lambda x: 1 + (1/2) * (np.sin(2*x))**3
g = lambda x: 3 + (1/2) * (np.cos(3*x))**5

# 2. Plotando as funções
plt.plot(x_vals, f(x_vals), label='f(x) = 1 + (1/2) * sin^3(2x)')
plt.plot(x_vals, g(x_vals), label='g(x) = 3 + (1/2) * cos^5(3x)')
plt.fill_between(x_vals, f(x_vals), g(x_vals), where=(f(x_vals) > g(x_vals)), color='gray', alpha=0.5)
plt.legend()
plt.title('Gráfico das funções f(x) e g(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# 3. Calculando a área entre as funções simbolicamente
x = sp.Symbol('x')
f_sym = 1 + (1/2) * sp.sin(2*x)**3
g_sym = 3 + (1/2) * sp.cos(3*x)**5
area_simbolica = sp.integrate(f_sym - g_sym, (x, 0, 2 * sp.pi))
print(f"Área exata entre as curvas: {area_simbolica.evalf()}")

# 4. Método de Monte Carlo
n_points = 100000
x_rand = np.random.uniform(0, 2*np.pi, n_points)
y_rand = np.random.uniform(min(g(x_vals)), max(f(x_vals)), n_points)

# Contando os pontos entre as funções
below_f = y_rand < f(x_rand)
above_g = y_rand > g(x_rand)
between_curves = below_f & above_g
area_monte_carlo = (between_curves.sum() / n_points) * (2*np.pi * (max(f(x_vals)) - min(g(x_vals))))
print(f"Área aproximada (Monte Carlo): {area_monte_carlo}")