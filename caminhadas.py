import numpy as np
import matplotlib.pyplot as plt

# Função para realizar uma caminhada aleatória em 2D em uma grade
def random_walk_2d_grid(N, a=1):
    # Passos possíveis: (a,0), (0,a), (-a,0), (0,-a)
    steps = np.array([[a, 0], [0, a], [-a, 0], [0, -a]])
    # Escolha aleatória dos passos
    indices = np.random.choice(4, size=N)
    walk = np.cumsum(steps[indices], axis=0)  # Soma cumulativa para as posições
    return walk

# Função para calcular a distância quadrática média
def mean_square_distance_2d(walk):
    return np.mean(np.sum(walk**2, axis=1))

# Simulações da caminhada aleatória em 2D
def simulate_2d_walks_grid(N, M, a=1):
    d2_mean = []
    for _ in range(M):
        walk = random_walk_2d_grid(N, a)
        d2_mean.append(mean_square_distance_2d(walk))
    return np.mean(d2_mean)

# Parâmetros do problema
N_values = [10**3, 10**4, 10**5, 10**6]  # Número de passos
M = 1000  # Número de simulações
a = 1  # Tamanho do passo

# Plotar para 2D e calcular a média da distância quadrática
for N in N_values:
    mean_d2 = simulate_2d_walks_grid(N, M, a)
    print(f"Média da distância quadrática para N={N}: {mean_d2}")

# Extensão para 3D (opcional)

# Função para realizar uma caminhada aleatória em 3D em uma grade
def random_walk_3d_grid(N, a=1):
    # Passos possíveis: (a,0,0), (0,a,0), (0,0,a), (-a,0,0), (0,-a,0), (0,0,-a)
    steps = np.array([[a, 0, 0], [0, a, 0], [0, 0, a], [-a, 0, 0], [0, -a, 0], [0, 0, -a]])
    # Escolha aleatória dos passos
    indices = np.random.choice(6, size=N)
    walk = np.cumsum(steps[indices], axis=0)  # Soma cumulativa para as posições
    return walk

# Função para calcular a distância quadrática média em 3D
def mean_square_distance_3d(walk):
    return np.mean(np.sum(walk**2, axis=1))

# Simulações da caminhada aleatória em 3D
def simulate_3d_walks_grid(N, M, a=1):
    d2_mean = []
    for _ in range(M):
        walk = random_walk_3d_grid(N, a)
        d2_mean.append(mean_square_distance_3d(walk))
    return np.mean(d2_mean)

# Extensão para 3D
mean_d2_3d = simulate_3d_walks_grid(10**4, M, a)
print(f"Média da distância quadrática para N=10^4 em 3D: {mean_d2_3d}")

# Exemplo de plot de uma caminhada aleatória em 2D
def plot_random_walk_2d(walk):
    plt.plot(walk[:, 0], walk[:, 1])
    plt.title("2D Random Walk")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True)
    plt.show()

# Executando um exemplo de caminhada e plotando
N_example = 10000
walk_example = random_walk_2d_grid(N_example, a)
plot_random_walk_2d(walk_example)
