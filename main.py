import numpy as np
import matplotlib.pyplot as plt

# Configuração do gerador de números aleatórios para reprodutibilidade
np.random.seed(42)
dias = np.arange(1, 31)

# ==============================================================================
# 🟢 1. FENÔMENOS ESTÁVEIS (Fáceis de Modelar)
# ==============================================================================

# Altura média dos estudantes (Variação mínima em torno de 1.65m)
altura_media = 1.65 + np.random.normal(0, 0.005, size=30)

# Tempo médio de deslocamento até a escola (Média de 25 min com pequenas variações)
tempo_transito = 25 + np.random.normal(0, 2, size=30)

# ==============================================================================
# 🔴 2. FENÔMENOS VOLÁTEIS (Difíceis de Modelar)
# ==============================================================================

# Cliques no vídeo mais assistido (Crescimento caótico e viralização rápida)
video_visualizacoes = np.zeros(30)
video_visualizacoes[0] = 1000
for t in range(1, 30):
    # Efeito multiplicativo simulando algoritmo e compartilhamento caótico
    fator_viral = np.random.choice([0.8, 1.1, 1.5, 3.0], p=[0.2, 0.4, 0.3, 0.1])
    video_visualizacoes[t] = video_visualizacoes[t-1] * fator_viral

# Preço da moeda estrangeira (Caminhada aleatória / Random Walk com alta oscilação)
preco_moeda = np.zeros(30)
preco_moeda[0] = 5.00  # Preço inicial
for t in range(1, 30):
    choque_mercado = np.random.normal(0, 0.15)  # Alta volatilidade por notícias
    preco_moeda[t] = max(0.1, preco_moeda[t-1] + choque_mercado)


# ==============================================================================
# 📊 PLOTAGEM DOS GRÁFICOS COMPARATIVOS
# ==============================================================================
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Comparação de Volatilidade: Modelos Estáveis vs Voláteis", fontsize=16, fontweight='bold')

# Gráfico 1: Altura Média
axs[0, 0].plot(dias, altura_media, color='green', marker='o', linewidth=2)
axs[0, 0].set_title("🟢 Altura Média dos Estudantes (Estável)")
axs[0, 0].set_ylabel("Altura (metros)")
axs[0, 0].set_ylim(1.60, 1.70)
axs[0, 0].grid(True, linestyle='--')

# Gráfico 2: Tempo de Deslocamento
axs[0, 1].plot(dias, tempo_transito, color='darkgreen', marker='s', linewidth=2)
axs[0, 1].set_title("🟢 Tempo de Deslocamento até a Escola (Estável)")
axs[0, 1].set_ylabel("Tempo (minutos)")
axs[0, 1].set_ylim(15, 35)
axs[0, 1].grid(True, linestyle='--')

# Gráfico 3: Vídeo Viral
axs[1, 0].plot(dias, video_visualizacoes, color='red', marker='^', linewidth=2)
axs[1, 0].set_title("🔴 Visualizações do Vídeo Mais Assistido (Volátil/Caótico)")
axs[1, 0].set_ylabel("Visualizações Acumuladas")
axs[1, 0].grid(True, linestyle='--')

# Gráfico 4: Preço da Moeda
axs[1, 1].plot(dias, preco_moeda, color='darkred', marker='d', linewidth=2)
axs[1, 1].set_title("🔴 Preço da Moeda Estrangeira (Volátil/Mercado)")
axs[1, 1].set_ylabel("Valor em R$")
axs[1, 1].grid(True, linestyle='--')

# Ajustes de layout e salvamento
plt.tight_layout()
plt.savefig("comparacao_modelos.png")
print("Gráfico 'comparacao_modelos.png' gerado com sucesso!")
plt.show()
