'''
 Cálculo de Calibração do Sensor de Temperatura DS18B20
 Autora: Juliana de Souza Bispo
'''

import numpy as np
import matplotlib.pyplot as plt

# Dados do usuário (extraídos da tabela), X: Leituras do Sensor DS18B20 (Média), X = np.array([5.46, 26.70, 68.63])
X = np.array([5.3, 5.4, 5.7, 26.7, 26.7, 26.7, 66.6, 68.3, 71])

# Y: Leituras do Termômetro TP101 (Referência/Valor Verdadeiro), Y = np.array([4.66, 26.80, 70.13])
Y = np.array([4.5, 4.6, 4.9, 26.8, 26.8, 26.8, 68.3, 69.9, 72.2])

# --- 1. Cálculo da Regressão Linear (Método dos Mínimos Quadrados) ---

# A regressão linear encontra a melhor reta y = m*x + b, onde x = Leitura do Sensor e y = Temperatura de Referência (Corrigida, numpy.polyfit(x, y, grau)
# O grau 1 indica uma reta (regressão linear simples)
m, b = np.polyfit(X, Y, 1)

print(f"--- Coeficientes Calculados ---")
print(f"Inclinação (m): {m:.4f}")
print(f"Intercepto (b): {b:.4f}")
print(f"Fórmula de Calibração: T_corrigida = {m:.4f} * T_DS18B20 + ({b:.4f})")
print("------------------------------\n")

# --- 2. Geração do Gráfico Comparativo ---

# Cria uma linha de valores x para plotar a reta calculada
X_reta = np.linspace(min(X) - 5, max(X) + 5, 100)

# Calcula os valores y da reta usando a fórmula: y = m*x + b
Y_reta = m * X_reta + b

# Plot
plt.figure(figsize=(10, 6))

# 1. Plotar os pontos de medição (Leitura Bruta vs. Referência)
plt.scatter(X, Y, color='blue', label='Dados de Medição (DS18B20 vs. TP101)', zorder=5)

# 2. Plotar a Reta de Calibração Calculada
plt.plot(X_reta, Y_reta, color='red', linestyle='-', label=f'Reta de Calibração (y = {m:.4f}x + {b:.4f})', zorder=2)

# 3. Plotar a Reta Ideal (Y = X) para referência (nenhum erro)
plt.plot(X_reta, X_reta, color='gray', linestyle='--', label='Reta Ideal (Sem Erro)')

plt.title('Calibração Multi-Ponto do Sensor DS18B20 por Regressão Linear')
plt.xlabel('Temperatura Bruta do Sensor DS18B20 (°C)')
plt.ylabel('Temperatura Corrigida / Referência TP101 (°C)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# --- 3. Teste de Compensação ---
print("--- Teste de Compensação com a Fórmula ---")
for ds18b20_val, tp101_val in zip(X, Y):
    corrigido = m * ds18b20_val + b
    print(f"Bruta: {ds18b20_val:.2f} | Ref: {tp101_val:.2f} | Corrigida: {corrigido:.2f} | Erro Corrigido: {(corrigido - tp101_val):.2f}")
