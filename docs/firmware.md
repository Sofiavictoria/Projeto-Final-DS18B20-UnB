# Firmware (Arduino)

## Bibliotecas necessárias

Instale as bibliotecas:

- **OneWire**
- **DallasTemperature**

## Exemplo mínimo

```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  Serial.println(tempC);
  delay(1000);
}



```
