# Experimento de Calibração

O procedimento experimental foi estruturado para caracterizar a resposta estática do sensor DS18B20, submetendo-o a três condições térmicas distintas e representativas: **água resfriada (ponto frio)**, **água à temperatura ambiente** e **água aquecida (ponto quente)**.

Esta abordagem prática permitiu verificar o comportamento do sensor cobrindo tanto as temperaturas ideais para o funcionamento de aquários quanto situações críticas de falha.

## Padrão de Referência
Para validação, utilizou-se o método de comparação direta com um padrão de referência, o **Termômetro Digital Tipo Espeto TP101**.

**Especificações Técnicas:**

- **Faixa de medição:** $-50^{\circ}C$ a $+300^{\circ}C$.
- **Resolução:** $0,1^{\circ}C$.
- **Exatidão:** $\pm1^{\circ}C$ (na faixa de $20^{\circ}C$ a $80^{\circ}C$).

## Modelo Analítico
O princípio de funcionamento interno do sensor baseia-se na equação analítica da tensão *bandgap* de silício. A diferença de tensão base-emissor ($\Delta V_{BE}$) utilizada para a conversão é descrita pela equação:

$$\Delta V_{BE} = \frac{kT}{q} \cdot \ln\left(\frac{I_{C2}}{I_{C1}}\right)$$

O experimento visa corrigir os desvios sistemáticos (ganho e offset) que ocorrem na implementação física desta equação.

## Procedimento Experimental
O experimento foi realizado seguindo rigorosamente os passos abaixo:

1.  **Preparação dos recipientes:** Foram utilizados três copos com água em diferentes condições térmicas: temperatura ambiente, água gelada do filtro e água aquecida.
2.  **Inserção dos sensores:** O sensor DS18B20 e o termômetro de referência TP101 foram imersos simultaneamente no mesmo copo, garantindo que não tocassem o fundo ou as paredes do recipiente.
3.  **Estabilização da leitura:** Cada sensor permaneceu imerso por **3 minutos**, permitindo que as medições se estabilizassem. Durante esse período, foram registradas leituras a cada 1 minuto.
4.  **Intervalo entre medições:** Após medir a temperatura de um copo, os sensores foram retirados e deixados em repouso por **10 minutos**, permitindo que retornassem à temperatura ambiente antes da próxima medição.
5.  **Repetição:** O mesmo processo foi repetido para os três copos, garantindo consistência.
6.  **Registro:** As medições obtidas foram anotadas para cálculo do erro percentual.

## Equação de Calibração Obtida
Após a coleta de dados e aplicação do método dos Mínimos Quadrados (Regressão Linear), chegou-se à seguinte fórmula de correção:

$$T_{corrigida} = 1.0357 \cdot T_{sensor} - 0.9344$$