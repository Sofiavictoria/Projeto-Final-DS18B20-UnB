/********************************************************************
* Leitura de Temperatura DS18B20 com Display LCD
*
* Exibe a temperatura no monitor serial e no display LCD I2C
* Sem calibração
*
* Autora: Sofia Victória Bispo da Silva
* Disciplina: Instrumentação Eletrônica - UnB
*********************************************************************/

// Bibliotecas
#include <OneWire.h>
#include <DallasTemperature.h>
#include <LiquidCrystal_I2C.h> // Biblioteca utilizada para fazer a comunicação com o display 16x2

// Definições de hardware
#define PINO_ONEWIRE 12 // Define pino do sensor
#define COLUNAS_LCD 16
#define LINHAS_LCD 2
#define ENDERECO_I2C 0x27

// Objetos
OneWire oneWire(PINO_ONEWIRE); // Cria um objeto OneWire
DallasTemperature sensor(&oneWire); // Informa a referencia da biblioteca dallas temperature para Biblioteca onewire
DeviceAddress enderecoSensor; // Cria um endereco temporario da leitura do sensor
LiquidCrystal_I2C lcd(ENDERECO_I2C, COLUNAS_LCD, LINHAS_LCD); // Inicializa o display com 16 colunas e 4 linhas

// Variáveis
float temperatura = 0.0;
unsigned long ultimoTempo = 0;
const unsigned long INTERVALO = 1000; // 1 segundo

void setup() {
  Serial.begin(9600); // Inicia a porta serial

  //Inicialização do display
  lcd.init(); // Inicia a comunicação com o display
  lcd.backlight(); // Liga a luz de fundo do display
  lcd.clear(); // Limpa o display
  lcd.print("Inicializando..."); // Imprime a mensagem inicial
  delay(3000);
  sensor.begin(); // Inicia o sensor
  
  //verificar se o sensor está presente no barramento
  if (!sensor.getAddress(enderecoSensor, 0)) {
    Serial.println("ERRO: Sensor nao detectado!");
    lcd.clear();
    lcd.setCursor(0,0); lcd.print("SENSOR NAO");
    lcd.setCursor(0,1); lcd.print("ENCONTRADO!");
    while(true); // Para execução se sensor não detectado
  }

  //Define resolução do sensor
  sensor.setResolution(enderecoSensor, 12);
  lcd.clear();
}

void loop() {
  //Atualiza a leitura apenas se o intevalo definido passou
  if (millis() - ultimoTempo >= INTERVALO) {
    ultimoTempo = millis(); //Atualiza a marca de tempo

    sensor.requestTemperatures(); //Solicita leitura de temperatura
    temperatura = sensor.getTempC(enderecoSensor); //Lê temeperatura 

    //Verifica se a leitura foi válida
    if (temperatura == DEVICE_DISCONNECTED_C) {
      Serial.println("ERRO: Leitura invalida!");
      lcd.clear();
      lcd.print("Leitura invalida");
      return; // Sai da função loop e tenta novamente na proxima iteração
    }

    // Mostra no Serial
    Serial.print("Temperatura: "); // Imprime a temperatura no monitor serial
    Serial.print(temperatura, 1); //Exibe com 1 casa decimal
    Serial.println(" °C");

    // Mostra no LCD
    lcd.clear();
    lcd.setCursor(0,0); // Coluna 0, linha 0
    lcd.print("Temp: ");
    lcd.print(temperatura,1); // Busca temperatura para dispositivo
    lcd.print((char)223); // Símbolo de grau
    lcd.print("C");
  }
  delay(2000); //Aguarda 2 segundos antes de fazer nova leitura (para não atualizar muito rapido)
}
