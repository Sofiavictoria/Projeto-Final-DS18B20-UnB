# Firmware (Arduino)

## Bibliotecas necessárias

Instale as bibliotecas:
```cpp
#include <OneWire.h>
#include <DallasTemperature.h>
#include <LiquidCrystal_I2C.h>
```

> - **OneWire** - Comunicação com o sensor.
> - **DallasTemperature** - Biblioteca utilizada pelo DS18B20.
> - **LiquidCrystal_I2C.h** - Biblioteca utilizada para fazer a comunicação com o display 16x2.

## Definiçoes dos pinos 
```cpp
#define PINO_ONEWIRE 12 // Pino conectado ao sensor DS18B20
#define COLUNAS_LCD 16   // Número de colunas do LCD
#define LINHAS_LCD 2     // Número de linhas do LCD
#define ENDERECO_I2C 0x27 // Endereço I2C do LCD
```
> - **PINO_ONEWIRE** - define o pino do Arduino conectado ao sensor.
> - **COLUNAS_LCD e LINHAS_LCD** - tamanho do display LCD (16x2)
> - **ENDERECO_I2C** - endereço do LCD no barramento I2C.

## Configuração do Sensor e LCD
```cpp
sensor.begin();
if (!sensor.getAddress(enderecoSensor, 0)) {
    lcd.clear();
    lcd.print("Sensor nao encontrado");
    while(true); // Para execução se sensor não encontrado
}
```
> Inicializa o sensor e verifica se ele está presente no barramento.
Se não estiver, mostra mensagem e interrompe o programa.

```cpp
// Define a resolução do sensor
sensor.setResolution(enderecoSensor, 12);
lcd.clear();
```
> Define a precisão de 12 bits para o sensor DS18B20 (0,0625°C).
Limpa o LCD antes de mostrar novos dados.



## Codigo sem calibração
O código completo deste projeto está disponível no GitHub:

[Veja o código completo aqui](https://github.com/seuusuario/seurepositorio)

## Codigo com calibração

```cpp
ssss
```