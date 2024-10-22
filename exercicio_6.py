import numpy as np
import matplotlib.pyplot as plt

# Função para calcular pi usando Monte Carlo
def calcular_pi_3d(n_pontos):
    dentro_da_esfera = 0

    for _ in range(n_pontos):
        # Gera pontos aleatórios no cubo [-1, 1] x [-1, 1] x [-1, 1]
        x, y, z = np.random.uniform(-1, 1, 3)

        # Verifica se o ponto está dentro da esfera de raio 1
        if x**2 + y**2 + z**2 <= 1:
            dentro_da_esfera += 1

    # A proporção entre pontos dentro da esfera e total aproxima o volume da esfera
    volume_esfera_aprox = (dentro_da_esfera / n_pontos) * 8
    pi_aprox = (3 * volume_esfera_aprox) / 4  # Volume da esfera = (4/3) * pi * r^3, com r = 1
    return pi_aprox

# Função para gerar gráfico e tabela de erro
def plotar_resultados(n_max):
    pontos = []
    pi_estimado = []
    erro = []
    pi_real = np.pi

    for n in range(100, n_max + 1, 100):
        pi_aprox = calcular_pi_3d(n)
        pi_estimado.append(pi_aprox)
        pontos.append(n)
        erro.append(abs(pi_real - pi_aprox))

    # Plotando o gráfico do erro
    plt.figure(figsize=(10, 5))
    plt.plot(pontos, erro, label="Erro")
    plt.xlabel("Número de Pontos")
    plt.ylabel("Erro |pi - pi estimado|")
    plt.title("Erro na estimativa de pi usando Monte Carlo (3D)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Função para plotar pontos em 3D
def plotar_pontos_3d(n_pontos):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    for _ in range(n_pontos):
        x, y, z = np.random.uniform(-1, 1, 3)
        # Verifica se o ponto está dentro da esfera
        if x**2 + y**2 + z**2 <= 1:
            ax.scatter(x, y, z, color='blue', alpha=0.3)
        else:
            ax.scatter(x, y, z, color='red', alpha=0.1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'{n_pontos} Pontos aleatórios no cubo')
    plt.show()

# Usando o código
n_max = 10000  # Número máximo de pontos
plotar_resultados(n_max)
plotar_pontos_3d(1000)