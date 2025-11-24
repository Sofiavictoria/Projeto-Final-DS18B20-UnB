## Passo 1 — Metodologia

**Procedimento resumido:**

1. Preparar três amostras: água gelada, ambiente, água quente.
2. Submergir o sensor DS18B20 e o termômetro de referência em cada amostra.
3. Aguardar 3 minutos para estabilização e registrar leituras a cada 1 minuto.
4. Repetir para cada condição, retornando o sensor ao ambiente entre amostras.

**Condições controladas:** temperatura ambiente registrada, tempo de estabilização fixo, mesma profundidade de imersão.

**Observação:** Anote hora, ambiente (T ambiente), e se houve flutuação visível.


---

## Passo 2 — Dados Coletados

A seguir as medições coletadas (exemplo de formato). Substitua pelos seus dados reais.

| Condição     | Rep 1 (Ref °C) | Rep 2 (Ref °C) | Rep 3 (Ref °C) | Média Ref (°C) | DS18B20 Rep1 | DS18B20 Rep2 | DS18B20 Rep3 | Média DS18B20 | Erro (%) |
|--------------|----------------|----------------|----------------|----------------|--------------|--------------|--------------|---------------|----------|
| Água gelada  | 5.1            | 5.0            | 5.1            | 5.07           | 4.8          | 4.9          | 4.7          | 4.80          | 5.3      |
| Ambiente     | 23.4           | 23.6           | 23.5           | 23.50          | 23.1         | 23.2         | 23.0         | 23.10         | 1.7      |
| Água quente  | 45.0           | 44.8           | 45.1           | 44.97          | 44.2         | 44.0         | 44.5         | 44.23         | 1.6      |

> Substitua a tabela acima pelos seus valores reais (arquivo `results/raw_data.csv`).

# Passo 3 — Curva de Calibração

A partir dos dados coletados, gere a curva de calibração (por exemplo, regressão linear):

![Curva de calibração](../results/calibration_curve.png)

**Interpretação:** explique a inclinação, offset e se há não-linearidade na faixa medida.
MD


# Passo 4 — Modelo de Compensação

Exemplo de modelo linear aplicado:

\`\`\`
Temperatura_corrigida = a * Temperatura_DS18B20 + b
\`\`\`

Coeficientes encontrados (exemplo):
- a = 1.02
- b = -0.35

**Implementação:** aplicar a e b no script Python que processa `raw_data.csv` e salvar `results/adjusted_data.csv`.
MD
