# Projeto de Calibração do Sensor DS18B20

Bem-vinda(o)! Esta é a documentação do projeto final da disciplina **Instrumentação Eletrônica para Engenharia — UnB (2025/2)**.

**Objetivo:** calibrar o sensor DS18B20, comparar com referência e implementar uma compensação digital.

- [Baixar relatório (PDF)](assets/Relatorio_Projeto_Final_DS18B20.pdf)

# Projeto Final: Calibração de Sensor de Temperatura

**Disciplina:** Instrumentação Eletrônica para Engenharia (FGA0132)  
**Instituição:** Universidade de Brasília (UnB)  
**Semestre:** 2025/2  
**Autoras:** Juliana de Souza Bispo e Sofia Victória Bispo da Silva

---

## Introdução

A medição precisa de temperatura é uma necessidade crítica em diversas áreas, abrangendo desde a automação industrial e dispositivos médicos de alta precisão até o fundamental monitoramento ambiental. Em muitos desses cenários, a confiabilidade dos dados é determinante para a segurança e eficiência dos processos.

### Motivação: Monitoramento de Aquários
Dentro deste contexto de monitoramento ambiental, uma aplicação prática crítica é o controle térmico de **aquários e ecossistemas aquáticos**. A estabilidade da temperatura é vital para a sobrevivência de espécies sensíveis, que muitas vezes não toleram variações bruscas ou erros de leitura superiores a 1°C. Para atender a essa demanda específica, torna-se necessário o uso de instrumentos que sejam, ao mesmo tempo, blindados contra a umidade e metrologicamente confiáveis, garantindo que o habitat seja mantido dentro dos parâmetros ideais de preservação da vida.

### O Sensor DS18B20
Para atender a essa demanda, o sensor **DS18B20** apresenta-se como uma solução prática e altamente confiável, notadamente por sua saída de dados digital e a disponibilidade de encapsulamentos robustos e à prova d'água (*waterproof*). Diferentemente de sensores analógicos, que tipicamente demandam circuitos adicionais para condicionamento de sinal e conversão, o DS18B20 realiza internamente todas as etapas de leitura, processamento e comunicação digital através do protocolo 1-Wire.

### O Problema e o Objetivo
Entretanto, a acurácia de qualquer instrumento de medição de baixo custo pode ser sutilmente afetada por variações no processo de fabricação. É por essa razão que a **calibração** emerge como um processo crucial para validar e garantir a precisão dos dados coletados.

Neste contexto, o presente trabalho se propõe a descrever e documentar um experimento detalhado de calibração estática do sensor DS18B20, visando validar e aplicar uma compensação digital para corrigir os desvios observados.