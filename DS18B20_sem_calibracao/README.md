# Relatório: Software de Aquisição de Temperatura


A nível de software, utilizamos um código simples em C, para podermos fazer os testes antes da compensação e mostrar as temperaturas medidas no Monitor Serial do aplicativo do Arduino e no display LCD I2C. O sistema foi inicialmente desenvolvido e validado utilizando uma
abordagem mista que combinou prototipagem física e simulação computacional no ambiente Tinkercad, permitindo a verificação do funcionamento do circuito antes da implementação física.
O algoritmo principal foi organizado em funções modulares, seguindo boas práticas de programação embedded, com inicialização robusta dos periféricos e tratamento de erros para garantir operação confiável do sistema.

### Pseudocódigo de Inicialização

``` {#lst:pseudocodigo_inicio style="arduinoStyle" caption="Pseudocódigo Inicialização" label="lst:pseudocodigo_inicio"}

// Bibliotecas
#include <OneWire.h>
#include <DallasTemperature.h>
#include <LiquidCrystal_I2C.h>

// Definicoees de hardware
#define PINO_ONEWIRE 12
#define COLUNAS_LCD 16
#define LINHAS_LCD 2
#define ENDERECO_I2C 0x27

// Objetos globais
OneWire oneWire(PINO_ONEWIRE);
DallasTemperature sensor(&oneWire);
DeviceAddress enderecoSensor;
LiquidCrystal_I2C lcd(ENDERECO_I2C, COLUNAS_LCD, LINHAS_LCD);

// Variaveis do sistema
float temperatura = 0.0;
unsigned long ultimoTempo = 0;
const unsigned long INTERVALO = 1000;
```
---------------------------------
### 1) Inicialização do Sistema (Setup) 

A função `setup()` implementa a sequência de inicialização completa dos periféricos, incluindo comunicação serial, display LCD e sensor de temperatura. Durante a inicialização, são realizadas verificações de hardware para detectar possíveis falhas, garantindo uma operação
confiável do sistema. Essas rotinas de verificação ajudam a identificar problemas no hardware antes que o sistema comece a capturar e exibir os dados.

``` {#lst:pseudocodigo_setup style="arduinoStyle" caption="Pseudocódigo setup" label="lst:pseudocodigo_setup"}

void setup() {
  Serial.begin(9600);
  
  // Inicializacao do display LCD
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.print("Inicializando...");
  delay(3000);
  
  sensor.begin();
  
  // Verificacao de presenca do sensor
  if (!sensor.getAddress(enderecoSensor, 0)) {
    Serial.println("ERRO: Sensor nao detectado!");
    lcd.clear();
    lcd.setCursor(0,0); lcd.print("SENSOR NAO");
    lcd.setCursor(0,1); lcd.print("ENCONTRADO!");
    while(true); // Para execução se sensor não detectado
  }

  // Configuracao da resolução do sensor
  sensor.setResolution(enderecoSensor, 12);
  lcd.clear();
}
```
----------------------------------------
### 2) Algoritmo Principal de Aquisição (Loop) 

A função `loop()` implementa o núcleo do sistema de aquisição, utilizando temporização baseada em `millis()` para leituras periódicas, evitando o uso de `delay()` bloqueante e garantindo responsividade do sistema.

``` {#lst:pseudocodigo_loop style="arduinoStyle" caption="Pseudocódigo loop" label="lst:pseudocodigo_loop"}
void loop() {
  // Atualiza a leitura apenas se o intervalo definido passou
  if (millis() - ultimoTempo >= INTERVALO) {
    ultimoTempo = millis();

    // Sequencia de aquisicao de temperatura
    sensor.requestTemperatures();
    temperatura = sensor.getTempC(enderecoSensor);

    // Verificacao de integridade dos dados
    if (temperatura == DEVICE_DISCONNECTED_C) {
      Serial.println("ERRO: Leitura invalida!");
      lcd.clear();
      lcd.print("Leitura invalida");
      return;
    }

    // Exibicao no monitor serial
    Serial.print("Temperatura: ");
    Serial.print(temperatura, 1);
    Serial.println(" °C");

    // Exibicao no display LCD
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Temp: ");
    lcd.print(temperatura,1);
    lcd.print((char)223); // Simbolo de grau
    lcd.print("C");
  }
  delay(2000);
}
}
```
-----------------------------
### 3) Características Técnicas da Implementação 

A arquitetura de software adotada apresenta as seguintes características
técnicas:

-   Resolução de medição: 12 bits (0.0625°C)

-   Intervalo de amostragem: 1 segundo (configurável)

-   Comunicação serial: 9600 bauds

-   Protocolo de sensor: 1-Wire com biblioteca `DallasTemperature`

-   Interface de display: I2C com biblioteca `LiquidCrystal_I2C`

-   Tratamento de erros: Verificação de conexão e validade de leitura
-----------------------------
### 4) Estratégias de Robustez Implementadas 
Foram incorporadas várias técnicas para garantir a confiabilidade do
sistema:

-   Verificação de endereçamento do sensor durante inicialização:
    Garantindo que o sensor correto seja identificado antes de começar
    as leituras.

-   Detecção de desconexão do dispositivo durante operação: O sistema
    verifica se o sensor continua conectado ao longo da operação, para
    evitar leituras erradas.

-   Limpeza e reposicionamento do display a cada atualização: O display
    LCD é limpo e reposicionado a cada nova leitura, garantindo uma
    exibição precisa e atualizada.

-   Uso de temporização não-bloqueante para manter responsividade: A
    temporização com `millis()` permite que o sistema continue
    responsivo durante a execução, evitando bloqueios causados por
    comandos como `delay()`.

-   Formatação consistente dos dados exibidos: Todos os dados são
    apresentados de forma uniforme, garantindo legibilidade e clareza na
    interface de usuário.

-------------------------------------------
### 5) Saídas do Sistema 
O software fornece saída dupla para os dados de temperatura:

-   Monitor Serial: Apresenta valores numéricos com *timestamp*
    implícito, permitindo o monitoramento das leituras ao longo do
    tempo.

-   Display LCD: Mostra a informação formatada com símbolo de grau
    Celsius ($^\circ$C), fornecendo uma interface visual local para o
    usuário.


Ambas as interfaces são atualizadas simultaneamente a cada ciclo de leitura, garantindo que o usuário tenha acesso às informações mais recentes de maneira eficiente.Esta implementação serve como base para a versão com calibração, mantendo a mesma estrutura fundamental enquanto adiciona as
funcionalidades de caracterização e compensação do sensor. Isso permitirá que o sistema alcance maior precisão e adaptabilidade a diferentes condições ambientais e características do sensor. 
