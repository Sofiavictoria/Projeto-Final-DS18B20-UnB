---

## Calibração e Análise de Erro do Sensor DS18B20 

Este documento detalha a metodologia computacional empregada para a calibração de um sensor de temperatura **DS18B20** utilizando o método de **Regressão Linear (Mínimos Quadrados)** e a subsequente análise de erro sistemático do sistema calibrado. Os procedimentos são implementados em dois *scripts* Python distintos, utilizando as bibliotecas `numpy` (para cálculo) e `matplotlib.pyplot` (para visualização).

---

### 1. Código [Calculo_Compensacao.py](https://github.com/Sofiavictoria/Projeto-Final-DS18B20-UnB/blob/main/Plots/Calculo_Compensacao.py): Determinação dos Coeficientes de Calibração

O primeiro estágio da calibração consiste em determinar a equação linear ótima que mapeia a leitura bruta do sensor ($X$) para a temperatura real de referência ($Y$).

#### 1.1. Metodologia (Regressão Linear Simples)

A **Regressão Linear Simples** busca encontrar a reta que minimiza a soma dos quadrados das distâncias verticais entre os pontos de dados e a reta. Esta reta é representada pela equação:

$$
Y = m \cdot X + b
$$

* **$X$**: Temperatura Bruta do Sensor DS18B20 (Variável Independente).
* **$Y$**: Temperatura Lida pelo Termômetro de Referência TP101 (Variável Dependente / Corrigida).
* **$m$**: Coeficiente Angular (Inclinação).
* **$b$**: Coeficiente Linear (Intercepto).



#### 1.2. Implementação em Python

O código utiliza a função **`numpy.polyfit(X, Y, 1)`** para calcular os coeficientes $m$ e $b$. O parâmetro `1` indica que o ajuste deve ser um polinômio de primeiro grau, ou seja, uma reta.

**Saída e Aplicação da Fórmula:**
O *script* imprime os coeficientes calculados e a **Fórmula de Calibração** resultante:
$$
T_{corrigida} = 1.0506 \cdot T_{DS18B20} + (-0.1706)
$$
*(Nota: Valores de exemplo baseados nos dados fornecidos).*

#### 1.3. Visualização

O gráfico gerado pelo Código 2 ilustra:

1.  Os **Pontos de Medição** ($X$ vs. $Y$) (em azul).
2.  A **Reta de Calibração** calculada (em vermelho). Esta reta representa a função ideal que deve ser aplicada ao sensor.
3.  A **Reta Ideal ($Y=X$)** (em cinza tracejado). Esta reta serve como referência para um sensor que não apresentaria erro (leitura bruta = leitura corrigida).

---

### 2. Código [Comparacao_Final.py](https://github.com/Sofiavictoria/Projeto-Final-DS18B20-UnB/blob/main/Plots/Comparacao_Final.py): Análise de Tendência e Erro Pós-Calibração

O segundo *script* utiliza um conjunto de dados reduzido (três pontos representativos: $\sim 6^{\circ}C$, $\sim 25^{\circ}C$, $\sim 40^{\circ}C$) para **quantificar o erro sistemático** antes e depois da calibração.

#### 2.1. Metodologia de Análise de Tendência

Em vez de calcular o erro ponto a ponto, o código calcula a **Reta de Tendência** para cada conjunto de dados (Referência, Bruto e Calibrado) em função de um índice sequencial:

$$
Reta(x) = m_{tend} \cdot índice + b_{tend}
$$

A reta de referência (a ideal) é comparada com as retas Bruta e Calibrada para isolar o **Erro Sistemático Tendencial** do sistema.

#### 2.2. Cálculo do Erro Sistemático

O **Erro Sistemático** é definido como a diferença entre a reta de tendência do sensor e a reta de tendência da Referência:

$$
Erro_{Bruto} = Reta_{Bruta} - Reta_{Referência}
$$
$$
Erro_{Calibrado} = Reta_{Calibrada} - Reta_{Referência}
$$

Este cálculo demonstra o desvio médio e a tendência de desvio do sensor ao longo de sua faixa de operação, o que é crucial para validação metrológica.

#### 2.3. Visualização e Comparação de Desempenho

O código gera um gráfico com dois subplots:

1.  **Curvas de Temperatura:** Plota os pontos medidos e as três **Retas de Tendência** (Referência, Bruta e Calibrada). A proximidade da Reta Calibrada com a Reta de Referência evidencia a eficácia da calibração.
2.  **Curvas de Erro Tendencial:** Plota as curvas de $Erro_{Bruto}$ e $Erro_{Calibrado}$. O objetivo da calibração é fazer com que a curva de $Erro_{Calibrado}$ se aproxime da linha de **Erro Zero (0)**.

#### 2.4. Métrica de Desempenho

O *script* calcula o **Desvio Absoluto Médio do Erro Tendencial (MAE)** para quantificar a melhoria na precisão:

* **MAE Bruto:** Reflete o erro médio antes da correção.
* **MAE Calibrado:** Reflete o erro médio após a aplicação da fórmula de calibração.

A redução significativa do MAE Calibrado em relação ao MAE Bruto é a evidência numérica da **eficácia da compensação** por regressão linear.

| Métrica | Valor (Exemplo) | Interpretação |
| :---: | :---: | :---: |
| MAE Bruto | $0.80^{\circ}C$ | Desvio médio inicial do sensor. |
| MAE Calibrado | $0.11^{\circ}C$ | Desvio médio após a correção, indicando **alta precisão**. |
