# Hardware Utilizado

##  Sensor Escolhido

![Sensor DS18B20](./imagens/sensor-de-temperatura-ds18b20-prova-d-agua.jpg){width="400px" style="display:block; margin:auto;"} 


**Sensor escolhido:** DS18B20 à prova d’água  
- Faixa de medição: -55°C a 125°C  
- Precisão: ±0,5°C  
- Interface: 1-Wire  
- Observação: fácil de calibrar com termômetro de referência

## Instrumento de referencia 

![TP101](./imagens/TP1011-1200x1200.jpg){width="400px" style="display:block; margin:auto;"} 

**Instrumento de referencia:** Termômetro Digital Tipo Espeto TP101

-  Faixa de Medição -50ºC a +300 ºC / -58ºF a +572 ºF;
-  Resolução: 0.1 ºC/ºF;
-  Exatidão: (+-1°C ) para a faixa (-20 a 80 °C);
---
## Componentes

| Componente               | Quantidade | Função                           |
|--------------------------|:---------:|---------------------------------|
| Arduino UNO              | 1         | Microcontrolador                |
| DS18B20 (à prova d'água) | 1         | Sensor de temperatura           |
| Resistor 4.7 kΩ          | 1         | Pull-up para barramento 1-Wire  |
| Termômetro culinario        | 1         | Referência de calibração        |
| Display LCD/I2C (16x2)   | 1         | Mostra temperatura em tempo real|

---

## Diagrama do Circuito

![Circuito](./imagens/esquematico_sensor_ds18b20_2025-11-24.png)
Figura 2 - Esquematico do circuito. Fonte: Autoria Própria,2025.

---


O sensor comunica-se através do protocolo **1-Wire**. O pino de dados (DQ) do sensor deve ser conectado a uma porta digital do Arduino, com um resistor de pull-up conectado ao VCC (5V).

| Componente | Pino Componente | Conexão Arduino | Observação |
| :--- | :--- | :--- | :--- |
| **DS18B20** | VCC (Vermelho) | 5V | Alimentação |
| **DS18B20** | GND (Preto) | GND | Terra |
| **DS18B20** | DATA (Amarelo) | D12 | Pino de Dados  |
| **Resistor** | 4.7k$\Omega$ | D12 e 5V | Pull-up entre Dados e VCC |
| **LCD I2C** | SDA | A4 | Dados I2C |
| **LCD I2C** | SCL | A5 | Clock I2C |

> **Observação 1:** O resistor de 4.7k$\Omega$ é crucial para a integridade do sinal digital no barramento 1-Wire

> **Observação 2:** Para displays I2C, verifique o endereço do módulo (normalmente 0x27 ou 0x3F) antes de programar.

---
##  Fotos do Protótipo
> Protótipo de teste
![Protótipo de teste](./imagens/prototipo2.jpeg)  
---
> Protótipo completo
![Protótipo completo](./imagens/prototipo1.jpeg)  


----
## Fotos do  teste
![Teste completo](./imagens/teste1.jpeg) 

![Teste completo](./imagens/teste2.jpeg) 
---
## Observações importantes

- Mantenha o sensor e o display protegidos de água, caso usados fora do laboratório.  
- Evite curtos entre os cabos.  
- Use cabos curtos ou blindados para leituras mais estáveis.  
- Certifique-se de ajustar contraste do display e verificar endereços I2C.  


