import numpy as np
import matplotlib.pyplot as plt

# Função para gerar uma caminhada aleatória em 2D
def random_walk_2d(N):
    x = np.cumsum(np.random.choice([-1, 1], size=N))  # Soma cumulativa para posição x
    y = np.cumsum(np.random.choice([-1, 1], size=N))  # Soma cumulativa para posição y
    return x, y

# Função para calcular a distância quadrática média
def mean_square_distance(x, y):
    return np.mean(x**2 + y**2)

# Simulações da caminhada aleatória em 2D
def simulate_2d_walks(N, M):
    d2_mean = []
    for _ in range(M):
        x, y = random_walk_2d(N)
        d2_mean.append(mean_square_distance(x, y))
    return np.mean(d2_mean)

# Função para caminhada aleatória em 3D
def random_walk_3d(N):
    x = np.cumsum(np.random.choice([-1, 1], size=N))  # Posição x
    y = np.cumsum(np.random.choice([-1, 1], size=N))  # Posição y
    z = np.cumsum(np.random.choice([-1, 1], size=N))  # Posição z
    return x, y, z

# Parâmetros do problema
N_values = [10**3, 10**4, 10**5, 10**6]  # Número de passos
M = 1000  # Número de simulações

# Plotar para 2D
for N in N_values:
    mean_d2 = simulate_2d_walks(N, M)
    print(f"Média da distância quadrática para N={N}: {mean_d2}")
