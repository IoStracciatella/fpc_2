import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para calcular pi em 3D usando o método de Monte Carlo
def monte_carlo_pi_3d(N):
    count_inside = 0
    points_inside = []
    points_outside = []
    
    # Gerar pontos aleatórios
    for _ in range(N):
        x, y, z = np.random.uniform(-1, 1, 3)  # Ponto aleatório no cubo [-1, 1] x [-1, 1] x [-1, 1]
        if x**2 + y**2 + z**2 <= 1:
            count_inside += 1  # Está dentro da esfera
            points_inside.append([x, y, z])
        else:
            points_outside.append([x, y, z])
    
    # Aproximar pi
    pi_approx = (count_inside / N) * 6  # Aproximando o volume da esfera em relação ao cubo
    return pi_approx, np.array(points_inside), np.array(points_outside)

# Função para calcular o erro e plota-lo
def calculate_and_plot_error_3d(N_values):
    pi_real = np.pi  # Valor real de pi
    pi_approximations = []
    errors = []

    # Calcular pi para diferentes valores de N
    for N in N_values:
        pi_mc, points_inside, points_outside = monte_carlo_pi_3d(N)
        pi_approximations.append(pi_mc)
        error = np.abs(pi_real - pi_mc)
        errors.append(error)

        # Plotar os pontos 3D
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Pontos dentro da esfera (verdes)
        ax.scatter(points_inside[:, 0], points_inside[:, 1], points_inside[:, 2], color='green', alpha=0.5, label='Dentro da Esfera')

        # Pontos fora da esfera (vermelhos, mais transparentes)
        ax.scatter(points_outside[:, 0], points_outside[:, 1], points_outside[:, 2], color='red', alpha=0.1, label='Fora da Esfera')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Pontos Monte Carlo - N={N}')
        plt.legend()
        plt.show()

    # Plotar erro em escala log10
    plt.figure(figsize=(10, 6))
    plt.plot(N_values, np.log10(errors), marker='o')
    plt.xlabel('N (Número de Realizações)')
    plt.ylabel('Erro (log10 |π - π_MC|)')
    plt.title('Erro do Método de Monte Carlo para Cálculo de π em 3D')
    plt.grid(True)
    plt.show()

    # Tabela de resultados
    print(f"{'N':>10} {'Pi Aproximado':>20} {'Erro':>20}")
    for i in range(len(N_values)):
        print(f"{N_values[i]:>10} {pi_approximations[i]:>20.10f} {errors[i]:>20.10f}")

# Definir os valores de N (número de realizações)
N_values = [100, 1000, 10000, 100000]

# Calcular e plotar os resultados
calculate_and_plot_error_3d(N_values)