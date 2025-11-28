## Análise Funcional e Metodologia de Calibração do Módulo de Aquisição de Temperatura

Este documento descreve a funcionalidade do código-fonte para aquisição de temperatura utilizando o sensor **DS18B20** e sua exibição em um display **LCD I2C (16x2)**, com foco especial no método de **compensação por regressão linear (calibração multi-ponto)** implementado.

-----

### 1\. Visão Geral da Funcionalidade

O código tem como objetivo principal monitorar a temperatura ambiente de forma contínua e precisa, empregando o seguinte fluxo operacional:

1.  **Inicialização:** Configuração da comunicação serial, do display LCD (endereço `0x27`) e do sensor DS18B20 (pino `D12`). Uma verificação crítica garante que o sensor seja detectado e configurado com **resolução de 12 bits** (máxima precisão).
2.  **Aquisição Sincronizada:** Utiliza o método não-bloqueante baseado em **`millis()`** para solicitar e ler a temperatura do DS18B20 em intervalos regulares de **1000 milissegundos (1 segundo)**.
3.  **Processamento:** A leitura direta do sensor (temperatura bruta) é submetida ao módulo de calibração para obter a temperatura corrigida.
4.  **Saída de Dados:** Os valores de temperatura bruta e calibrada são exibidos simultaneamente no **Monitor Serial** e no **Display LCD 16x2**.

-----

### 2\. Implementação e Ênfase na Calibração/Compensação

A precisão do sistema é otimizada pela aplicação de uma correção algorítmica baseada em dados de referência obtidos em laboratório, caracterizando uma **compensação por regressão linear**.

#### 2.1 Modelo Matemático de Compensação

A calibração do sensor é realizada através de uma equação linear que relaciona a leitura bruta do sensor ($T_{bruta}$) com o valor de temperatura corrigido ($T_{corrigida}$):

$$
T_{corrigida} = m \cdot T_{bruta} + b
$$

Onde:

  * **$T_{corrigida}$** é a temperatura compensada que reflete o valor real.
  * **$T_{bruta}$** é o valor lido diretamente do sensor DS18B20.
  * **$m$** (Coeficiente Angular) e **$b$** (Coeficiente Linear) são os coeficientes de calibração obtidos por regressão linear a partir de múltiplos pontos de medição comparados com um termômetro de referência (padrão rastreável).

#### 2.2 Coeficientes Aplicados

Os coeficientes definidos no código para esta compensação são:

| Variável | Constante C++ | Valor |
| :---: | :---: | :---: |
| Coeficiente Angular ($m$) | `M_COEFICIENTE` | **1.0357** |
| Coeficiente Linear ($b$) | `B_COEFICIENTE` | **-0.9344** |

#### 2.3 Função de Execução

A aplicação do modelo é encapsulada na função dedicada **`aplicarCalibracao(float leituraBruta)`**, garantindo a modularidade e clareza do código:

```cpp
float aplicarCalibracao(float leituraBruta) {
  // T_corrigida = m * T_bruta + b
  return (M_COEFICIENTE * leituraBruta) + B_COEFICIENTE;
}
```

No laço principal (`loop`), a temperatura bruta lida (`temperatura_bruta`) é imediatamente processada por esta função, gerando a `temperatura_calibrada`, que é o dado primário de interesse para o relatório.

### 3\. Detalhes da Saída

O código é configurado para apresentar ao usuário os dois valores distintos, permitindo a **rastreabilidade e validação** da compensação:

  * **LCD (Linha 0):** Mostra a **T Bruta**, permitindo avaliar o desvio inicial do sensor.
  * **LCD (Linha 1):** Mostra a **T Calibrada**, que representa a medição corrigida e o resultado final do sistema de instrumentação.
  * **Serial Monitor:** Exibe ambos os valores na forma: `Temperatura: XX.XX °C`.

-----

### Autoras

  * Juliana de Souza Bispo
  * Sofia Victória Bispo da Silva

**Disciplina:** Instrumentação Eletrônica - Universidade de Brasília (UnB)

-----
