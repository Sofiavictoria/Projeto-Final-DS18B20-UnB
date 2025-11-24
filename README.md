# ❄️🔥 Projeto de Calibração do Sensor DS18B20  

![Arduino](https://img.shields.io/badge/Hardware-Arduino_Uno-00979D?style=for-the-badge&logo=arduino&logoColor=white)
![C++](https://img.shields.io/badge/Code-C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)

---

<div align="center">
  <img src="simulador.png" width="600px">
  <p><em>Montagem do sensor DS18B20 com Arduino no simulador Wokwi.</em></p>
</div>

---

## 📌 Sobre o Projeto

Este repositório faz parte do projeto final da disciplina **Instrumentação Eletrônica para Engenharia — UnB (2025/2)**.  

O objetivo é realizar a **calibração estática do sensor digital DS18B20**, compará-lo com um instrumento de referência e implementar um **modelo matemático de compensação** para melhorar sua precisão na medição da temperatura.

Após a calibração, o sensor é utilizado para monitoramento ambiental em tempo real.

---

## 🎯 Objetivo

- Avaliar o desempenho do sensor DS18B20 antes e depois do processo de calibração.  
- Implementar um método de compensação digital baseado nos dados obtidos experimentalmente.  

---

## ⚙️ Funcionalidades

- Leitura digital de temperatura via protocolo One-Wire  
- Registro experimental e curva de calibração  
- Ajuste matemático (regressão linear ou polinomial)  
- Compensação dos valores medidos  
- Comparação do erro percentual antes × depois  

---

## 🧪 Hardware Utilizado

| Componente | Quantidade | Função |
|-----------|:---------:|--------|
| Arduino UNO | 1 | Microcontrolador |
| Sensor DS18B20 (à prova d’água) | 1 | Sensor primário |
| Resistor 4.7kΩ | 1 | Pull-up no barramento 1-Wire |
| Termômetro culinario | 1 | Referência de calibração |
| Display i2c | 1 | esqueci a funçao |

---

## 🧩 Pinagem do Sensor DS18B20


---

## 👩‍🔬 Autores

| Nome | Curso |
|------|--------|
| Sofia Vitória Bispo da Silva | Engenharia Eletronica |
| Juliana de Souza Bispo | Engenharia Eletronica |

**Orientação:** Profa. Claudia Patricia Ochoa Diaz — Universidade de Brasília.

---

📌 *Este repositório será atualizado conforme o andamento do relatório e validação dos resultados finais.*


