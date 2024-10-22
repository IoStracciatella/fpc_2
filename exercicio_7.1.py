# Caminhadas Aleatórias com Cálculo de Distâncias

import numpy as np
import matplotlib.pyplot as plt

# Função que realiza uma caminhada aleatória de N passos
def movimentacao(N):
    x, y = 0, 0
    pos_x = [x]
    pos_y = [y]

    for i in range(N):
        direcao = np.random.randint(1, 5)
        if direcao == 1:
            y += 1
        elif direcao == 2:
            y -= 1
        elif direcao == 3:
            x -= 1
        elif direcao == 4:
            x += 1

        pos_x.append(x)
        pos_y.append(y)

    return pos_x, pos_y

# Função que calcula a distância quadrática média
def calcular_distancia_quadratica_media(N, M):
    distancias_quadraticas = np.zeros(N + 1)

    for _ in range(M):  # Faz M realizações da caminhada aleatória
        pos_x, pos_y = movimentacao(N)
        for t in range(N + 1):
            distancia2 = (pos_x[t] - pos_x[0]) ** 2 + (pos_y[t] - pos_y[0]) ** 2
            distancias_quadraticas[t] += distancia2

    # Calcula a média das distâncias quadráticas para cada passo
    distancias_quadraticas /= M

    return distancias_quadraticas

# Parâmetros
M_valores = [10, 100]  # Quantidade de realizações
N = 10**4  # Número de passos

# Calcula e plota a distância quadrática média para cada valor de M
for M in M_valores:
    distancias_quadraticas = calcular_distancia_quadratica_media(N, M)
    
    plt.figure(figsize=(8, 6))
    plt.plot(range(N + 1), distancias_quadraticas, label=f"{M} realizações")
    plt.title(f"Distância Quadrática Média com {M} realizações e {N} passos")
    plt.xlabel('Número de passos (t)')
    plt.ylabel('Distância Quadrática Média $d_m^2(t)$')
    plt.grid(True)
    plt.legend()
    plt.show()