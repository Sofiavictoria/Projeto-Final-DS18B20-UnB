'''
Análise de Tendência e Erro por Regressão Linear.

O código calcula a reta de tendência (regressão) para a Referência (termomemtro TP101), o Sensor DS18B20 Bruto
e o Sensor DS18B20 Calibrado, e plota as retas para comparação e o cálculo do Erro Sistemático.

Autora: Juliana de Souza Bispo
'''

import numpy as np
import matplotlib.pyplot as plt

# --- DADOS DE ENTRADA ---
# Y: Leituras do Termômetro de Referência (Valor Verdadeiro) 
Y = np.array([6.1, 25.2, 40.3])

# X: Leituras do Sensor de Temperatura Bruto (Sem Calibração) 
X = np.array([5.3, 25.3, 41.8])

# T_cal: Leituras do Sensor Calibrado 
T_cal = np.array([5.7, 25.2, 40.1])

# Índice de medição para plotagem (Eixo X nos gráficos)
indices = np.arange(len(X))

# Rótulos customizados para o Eixo X (Faixas de Temperatura)
custom_labels = ['~6°C', '~25°C', '~40°C']

# --- 1. CÁLCULO DAS RETAS DE TENDÊNCIA (REGRESSÃO) ---
# Calcula a regressão de cada vetor em função do índice de medição (índices)

# Reta de Referência (Y)
m_ref, b_ref = np.polyfit(indices, Y, 1)
Y_fit = m_ref * indices + b_ref

# Reta do Sensor Bruto (X)
m_bruto, b_bruto = np.polyfit(indices, X, 1)
X_fit = m_bruto * indices + b_bruto

# Reta do Sensor Calibrado (T_cal)
m_cal, b_cal = np.polyfit(indices, T_cal, 1)
T_cal_fit = m_cal * indices + b_cal

# --- 2. CÁLCULO DO ERRO BASEADO NAS RETAS DE TENDÊNCIA ---
# Erro = Reta do Sensor - Reta de Referência

# Erro Bruto baseado na reta
Erro_bruto_fit = X_fit - Y_fit

# Erro Calibrado baseado na reta
Erro_calibrado_fit = T_cal_fit - Y_fit

# --- 3. GERAÇÃO DOS GRÁFICOS COMPARATIVOS ---

# Configura dois subplots: o superior para as temperaturas e o inferior para os erros
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
fig.suptitle('Análise de Tendência e Erro Sistemático do Sensor de Temperatura', fontsize=16)

# --- Subplot 1: Curvas de Temperatura (Retas de Tendência e Pontos Medidos) ---

# Plotar os pontos medidos (Scatters) para contexto
ax1.scatter(indices, Y, color='blue', marker='o', alpha=0.5, label='Pontos Medidos (Referência)')
ax1.scatter(indices, X, color='red', marker='^', alpha=0.5, label='Pontos Medidos (Sensor Bruto)')
ax1.scatter(indices, T_cal, color='green', marker='s', alpha=0.5, label='Pontos Medidos (Sensor Calibrado)')

# Plotar as Retas de Tendência (Linhas sólidas)
ax1.plot(indices, Y_fit, color='blue', linewidth=3, linestyle='-', label=f'Reta Referência (y={m_ref:.2f}x+{b_ref:.2f})')
ax1.plot(indices, X_fit, color='red', linewidth=2, linestyle='--', label=f'Reta Bruta (y={m_bruto:.2f}x+{b_bruto:.2f})')
ax1.plot(indices, T_cal_fit, color='green', linewidth=2, linestyle='-', label=f'Reta Calibrada (y={m_cal:.2f}x+{b_cal:.2f})')

ax1.set_title('Retas de Tendência de Temperatura ao Longo das Faixas de Medição')
ax1.set_ylabel('Temperatura (°C)')
# O ax1 compartilha o X, mas não precisa de rótulos visíveis, só a parte de baixo (ax2)
ax1.set_xticks(indices)
ax1.grid(True, which='both', linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

# --- Subplot 2: Curvas de Erro (Quantificação do Desvio Tendencial) ---
# Plota o erro calculado entre as retas de tendência
ax2.plot(indices, Erro_bruto_fit, color='red', linewidth=2, marker='^', linestyle='--', label='Erro Sistemático Bruto (Reta Bruta - Reta Ref.)')
ax2.plot(indices, Erro_calibrado_fit, color='green', linewidth=2, marker='s', linestyle='-', label='Erro Sistemático Calibrado (Reta Cal. - Reta Ref.)')

ax2.axhline(0, color='gray', linestyle='-', linewidth=1.5, label='Erro Zero (Ideal)') # Linha de erro zero
ax2.set_xlabel('Faixa de Temperatura')
ax2.set_ylabel('Erro Tendencial (°C)')
ax2.set_title('Erro Sistemático Calculado a partir das Retas de Tendência')
ax2.grid(True, which='both', linestyle=':', alpha=0.6)
ax2.legend(loc='upper left')

# Configura os rótulos do eixo X com as faixas de temperatura
ax2.set_xticks(indices)
# Rotação ajustada para 0 para deixar os rótulos retos
ax2.set_xticklabels(custom_labels, rotation=0) 

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# --- 4. TABELA DE RESUMO E ANÁLISE DE ERRO ---

print("\n--- Equações das Retas de Tendência ---")
print(f"Referência (Y): y = {m_ref:.4f}x + {b_ref:.4f}")
print(f"Sensor Bruto (X): y = {m_bruto:.4f}x + {b_bruto:.4f}")
print(f"Sensor Calibrado (T_cal): y = {m_cal:.4f}x + {b_cal:.4f}")

print("\n--- Tabela de Erro Sistemático (Baseado nas Retas) ---")
print("{:<5} | {:<12} | {:<10} | {:<10}".format(
    "IDX", "Ref (Y_fit)", "Erro Bruto", "Erro Calib."
))
print("-" * 45)

for i in range(len(indices)):
    print("{:<5} | {:<12.2f} | {:<10.2f} | {:<10.2f}".format(
        i+1, Y_fit[i], Erro_bruto_fit[i], Erro_calibrado_fit[i]
    ))

print("-" * 45)
mae_bruto_fit = np.mean(np.abs(Erro_bruto_fit))
mae_calibrado_fit = np.mean(np.abs(Erro_calibrado_fit))

print(f"Desvio Absoluto Médio do Erro Tendencial Bruto: {mae_bruto_fit:.3f} °C")
print(f"Desvio Absoluto Médio do Erro Tendencial Calibrado: {mae_calibrado_fit:.3f} °C")
