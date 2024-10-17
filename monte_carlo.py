import numpy as np
import matplotlib.pyplot as plt

# Função para calcular pi usando o método de Monte Carlo
def monte_carlo_pi(N):
    count_inside = 0
    
    # Gerar pontos aleatórios
    for _ in range(N):
        x, y = np.random.uniform(-1, 1, 2)  # Ponto aleatório no quadrado [-1, 1] x [-1, 1]
        if x**2 + y**2 <= 1:
            count_inside += 1  # Está dentro do círculo
    
    # Aproximar pi
    pi_approx = 4 * count_inside / N
    return pi_approx

# Função para calcular o erro e plota-lo
def calculate_and_plot_error(N_values):
    pi_real = np.pi  # Valor real de pi
    pi_approximations = []
    errors = []

    # Calcular pi para diferentes valores de N
    for N in N_values:
        pi_mc = monte_carlo_pi(N)
        pi_approximations.append(pi_mc)
        error = np.abs(pi_real - pi_mc)
        errors.append(error)

    # Plotar erro em escala log10
    plt.figure(figsize=(10, 6))
    plt.plot(N_values, np.log10(errors), marker='o')
    plt.xlabel('N (Número de Realizações)')
    plt.ylabel('Erro (log10 |π - π_MC|)')
    plt.title('Erro do Método de Monte Carlo para Cálculo de π')
    plt.grid(True)
    plt.show()

    # Tabela de resultados
    print(f"{'N':>10} {'Pi Aproximado':>20} {'Erro':>20}")
    for i in range(len(N_values)):
        print(f"{N_values[i]:>10} {pi_approximations[i]:>20.10f} {errors[i]:>20.10f}")

# Definir os valores de N (número de realizações)
N_values = [100, 1000, 10000, 100000, 1000000]

# Calcular e plotar os resultados
calculate_and_plot_error(N_values)