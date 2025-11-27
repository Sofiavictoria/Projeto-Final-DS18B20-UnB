/********************************************************************
* Leitura de Temperatura DS18B20 com Display LCD e Calibração
*
* Exibe a temperatura no monitor serial e no display LCD I2C
* Com compensação por regressão linear (multi-ponto)
*
* Autoras: Sofia Victória Bispo da Silva e Juliana de Souza Bispo
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

// --- Coeficientes de Calibração (Fórmula: T_corrigida = m*T_bruta + b) ---
// Valores fornecidos: m = 1.0357, b = -0.9344
const float M_COEFICIENTE = 1.0357;
const float B_COEFICIENTE = -0.9344;

// Objetos
OneWire oneWire(PINO_ONEWIRE); // Cria um objeto OneWire
DallasTemperature sensor(&oneWire); // Informa a referencia da biblioteca dallas temperature para Biblioteca onewire
DeviceAddress enderecoSensor; // Cria um endereco temporario da leitura do sensor
LiquidCrystal_I2C lcd(ENDERECO_I2C, COLUNAS_LCD, LINHAS_LCD); // Inicializa o display com 16 colunas e 4 linhas

// Variáveis
float temperatura_bruta = 0.0;
float temperatura_calibrada = 0.0;
unsigned long ultimoTempo = 0;
const unsigned long INTERVALO = 1000; // 1 segundo

/**
 * @brief Aplica a fórmula de compensação multi-ponto.
 *
 * @param leituraBruta A leitura direta do sensor DS18B20.
 * @return float A temperatura corrigida e compensada.
 */
float aplicarCalibracao(float leituraBruta) {
  // T_corrigida = m * T_bruta + b
  return (M_COEFICIENTE * leituraBruta) + B_COEFICIENTE;
}


void setup() {
  Serial.begin(9600); // Inicia a porta serial

  // Inicialização do display
  lcd.init(); // Inicia a comunicação com o display
  lcd.backlight(); // Liga a luz de fundo do display
  lcd.clear(); // Limpa o display
  lcd.print("Inicializando..."); // Imprime a mensagem inicial
  delay(3000);
  sensor.begin(); // Inicia o sensor
  
  // verificar se o sensor está presente no barramento
  if (!sensor.getAddress(enderecoSensor, 0)) {
    Serial.println("ERRO: Sensor nao detectado!");
    lcd.clear();
    lcd.setCursor(0,0); lcd.print("SENSOR NAO");
    lcd.setCursor(0,1); lcd.print("ENCONTRADO!");
    while(true); // Para execução se sensor não detectado
  }

  // Define resolução do sensor
  sensor.setResolution(enderecoSensor, 12);
  lcd.clear();
  Serial.println("Calibracao Aplicada: T_corr = 1.0357 * T_bruta - 0.9344");
}

void loop() {
  // Atualiza a leitura apenas se o intevalo definido passou
  if (millis() - ultimoTempo >= INTERVALO) {
    ultimoTempo = millis(); // Atualiza a marca de tempo

    sensor.requestTemperatures(); // Solicita leitura de temperatura
    temperatura_bruta = sensor.getTempC(enderecoSensor); // Lê temperatura 

    // Verifica se a leitura foi válida
    if (temperatura_bruta == DEVICE_DISCONNECTED_C) {
      Serial.println("ERRO: Leitura invalida!");
      lcd.clear();
      lcd.print("Leitura invalida");
      return; // Sai da função loop e tenta novamente na proxima iteração
    }
    
    // --- PASSO PRINCIPAL: APLICAÇÃO DA CALIBRAÇÃO ---
    temperatura_calibrada = aplicarCalibracao(temperatura_bruta);

    // Mostra no Serial
    Serial.print("Bruta: ");
    Serial.print(temperatura_bruta, 2); 
    Serial.print(" °C | Calibrada: ");
    Serial.print(temperatura_calibrada, 2); // Exibe com 2 casas decimais
    Serial.println(" °C");

    // Mostra no LCD
    lcd.clear();
    lcd.setCursor(0,0); // Coluna 0, linha 0
    lcd.print("T Bruta: ");
    lcd.print(temperatura_bruta,1); // Busca temperatura bruta
    lcd.print("C");

    lcd.setCursor(0,1); // Coluna 0, linha 1
    lcd.print("T Calibrada: ");
    lcd.print(temperatura_calibrada,1); // Busca temperatura calibrada
    lcd.print((char)223); // Símbolo de grau
    lcd.print("C");
  }
  // Foi removido o delay(2000) no final para evitar duplicar a espera
  // já que o controle de tempo está no if (millis() - ultimoTempo >= INTERVALO).
}
