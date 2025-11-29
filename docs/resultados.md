# Resultados e Discussão

## Dados de Calibração (Antes da Compensação)
A tabela abaixo apresenta os dados coletados comparando o sensor DS18B20 (sem calibração) com a referência TP101.

| Condição | Ref. TP101  | Sensor DS18B20  | Erro (%) | Desvio |
| :--- | :--- | :--- | :--- | :--- |
| **Fria** | 4,66 | 5,46 | 17,16% | -0,8 |
| **Natural** | 26,80 | 26,70 | 0,37% | +0,1 |
| **Quente** | 70,13 | 68,63 | 2,13% | +1,5 |
*[Fonte: Tabela I do Relatório]*.

Nota-se um comportamento não-linear nos erros, variando de -0,8°C (leitura maior que a real) no frio para +1,5°C (leitura menor que a real) no quente.

## Equação de Correção
Utilizando o método dos Mínimos Quadrados (Regressão Linear), obteve-se a seguinte função de transferência para o sensor calibrado:

$$T_{corrigida} = 1.0357 \cdot T_{sensor} - 0.9344$$

## Validação (Depois da Compensação)
Após implementar a equação acima no firmware, o sistema foi reavaliado.

| Condição | Ref. TP101 | Sensor Calibrado | Desvio Residual |
| :--- | :--- | :--- | :--- |
| **Fria** | 6,1°C | 5,7°C | 0,4°C |
| **Natural** | 25,2°C | 25,2°C | 0,0°C |
| **Quente** | 40,3°C | 40,2°C | 0,1°C |
*[Fonte: Tabela III do Relatório]*.

### Melhoria de Desempenho
* O desvio médio global foi reduzido de **0,85°C** para **0,20°C**.
* Isso representa uma melhoria de aproximadamente **76%** na precisão.

## Conclusão
O sensor calibrado atende aos requisitos para monitoramento de aquários, garantindo leituras com erro inferior a 0,5°C na faixa de operação usual.