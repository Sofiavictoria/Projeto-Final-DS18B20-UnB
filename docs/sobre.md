# Sobre o Projeto

## Resumo
Este projeto visa a instrumentação e calibração de um sistema de medição de temperatura utilizando o sensor digital **DS18B20**. O trabalho aborda desde a montagem do hardware até a implementação de algoritmos de compensação via software para mitigar erros de fabricação e garantir alta confiabilidade metrológica.

## Motivação
A medição precisa de temperatura é fundamental em diversos cenários, mas a motivação prática deste trabalho concentra-se no **monitoramento térmico de aquários e ecossistemas aquáticos**.
- A estabilidade térmica é vital para a saúde de peixes e corais.
- Muitas espécies não toleram variações bruscas ou erros de leitura superiores a  $5^{\circ}C$ em casos menos críticos.
- Sensores de baixo custo sem calibração podem apresentar desvios que comprometem a segurança biológica do habitat.

## Objetivos
O objetivo principal é transformar um sensor comercial comum em um instrumento de maior exatidão.

1.  **Caracterizar** a resposta do sensor em três faixas de temperatura (Fria, Ambiente, Quente).
2.  **Modelar** o erro sistemático através de Regressão Linear.
3.  **Implementar** a compensação digital no firmware do microcontrolador.
4.  **Validar** a melhoria de desempenho comparando com um termômetro de referência padrão.

## O Sensor DS18B20
O componente escolhido foi o **DS18B20** devido ao seu encapsulamento à prova d'água e comunicação digital via protocolo 1-Wire, que simplifica a integração de múltiplos sensores sem necessidade de conversores analógico-digitais externos.