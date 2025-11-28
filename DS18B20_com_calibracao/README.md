# 🌡️ Leitura de Temperatura DS18B20 com Calibração (Arduino)

Este projeto demonstra a leitura da temperatura ambiente usando o sensor digital **DS18B20** e a exibição dos valores, brutos e calibrados, em um **Display LCD I2C (16x2)**.

A principal característica deste código é a aplicação de uma **compensação por regressão linear (calibração multi-ponto)** para corrigir possíveis desvios na leitura do sensor.

## ✨ Características

  * **Sensor DS18B20:** Leitura de temperatura digital de alta precisão.
  * **Display LCD 16x2 I2C:** Exibição clara dos dados.
  * **Comunicação OneWire:** Utiliza apenas um pino digital para comunicação com o sensor.
  * **Calibração Integrada:** Aplica uma fórmula de regressão linear para fornecer uma medição mais precisa (**Tabela de Calibração** abaixo).
  * **Controle de Tempo:** Utiliza a função `millis()` para leituras em intervalos regulares, evitando o uso da função `delay()` e otimizando o código.

## 🧮 Calibração Aplicada

O sensor foi calibrado usando o método de regressão linear (multi-ponto) para ajustar a leitura bruta (**$T_{bruta}$**) a um valor corrigido (**$T_{corrigida}$**).

A fórmula de compensação utilizada é:

$$
T_{corrigida} = m \cdot T_{bruta} + b
$$

### Coeficientes de Calibração

| Variável | Coeficiente | Valor |
| :---: | :---: | :---: |
| **m** | Angular | `1.0357` |
| **b** | Linear | `-0.9344` |

O código define estas constantes como:

```cpp
const float M_COEFICIENTE = 1.0357;
const float B_COEFICIENTE = -0.9344;
```

## 🛠️ Hardware Necessário

  * Placa Arduino (ex: UNO, Nano).
  * Sensor de Temperatura **DS18B20** (com resistor *pull-up* de 4.7kΩ).
  * Display LCD **16x2 com módulo I2C** (endereço I2C comum: `0x27` ou `0x3F`).
  * Fios para conexão.

### Conexões

| Componente | Pino do Componente | Pino do Arduino | Observação |
| :---: | :---: | :---: | :---: |
| **DS18B20** | DATA | D12 | Requer resistor de 4.7kΩ (pull-up) |
| **LCD I2C** | SDA | A4 (ou SDA da sua placa) | |
| **LCD I2C** | SCL | A5 (ou SCL da sua placa) | |

## ⚙️ Bibliotecas

Este projeto requer as seguintes bibliotecas para compilação e funcionamento:

1.  **`OneWire`**: Para comunicação com o barramento OneWire do DS18B20.
      * *Instalação via Gerenciador de Bibliotecas:* Pesquise por `OneWire`.
2.  **`DallasTemperature`**: Para facilitar a leitura e manipulação do sensor DS18B20.
      * *Instalação via Gerenciador de Bibliotecas:* Pesquise por `DallasTemperature`.
3.  **`LiquidCrystal_I2C`**: Para controlar o Display LCD via interface I2C.
      * *Instalação via Gerenciador de Bibliotecas:* Pesquise por `LiquidCrystal_I2C`.

## 💻 Estrutura do Código

### 1\. Definições e Inicialização (`setup`)

  * O código inicia a comunicação **Serial** (9600 bps) e o **Display LCD**.
  * Verifica a presença do sensor **DS18B20** no barramento OneWire. Se o sensor não for encontrado, o programa para e exibe uma mensagem de erro no LCD e no Serial Monitor.
  * Define a resolução de leitura do DS18B20 para **12 bits** (máxima precisão).

### 2\. Função de Calibração

A função `aplicarCalibracao(float leituraBruta)` implementa a fórmula de regressão linear e é o cerne do processo de compensação:

```cpp
float aplicarCalibracao(float leituraBruta) {
  // T_corrigida = m * T_bruta + b
  return (M_COEFICIENTE * leituraBruta) + B_COEFICIENTE;
}
```

### 3\. Loop Principal (`loop`)

  * **Controle de Tempo:** A leitura é realizada apenas a cada **1000 milissegundos (1 segundo)**, conforme definido pela constante `INTERVALO`.
  * **Leitura:** O sensor solicita e obtém a `temperatura_bruta`.
  * **Validação:** Verifica se a leitura foi válida (não retornou `DEVICE_DISCONNECTED_C`).
  * **Aplicação da Calibração:** Chama a função `aplicarCalibracao()` para obter a `temperatura_calibrada`.
  * **Exibição:**
      * Os valores de temperatura bruta e calibrada são impressos no **Serial Monitor** com 2 casas decimais.
      * O **Display LCD** exibe a temperatura bruta na primeira linha e a temperatura calibrada (com o símbolo de grau `°`) na segunda linha.

-----

### Autoras

  * Sofia Victória Bispo da Silva
  * Juliana de Souza Bispo

**Disciplina:** Instrumentação Eletrônica - Universidade de Brasília (UnB)

-----

