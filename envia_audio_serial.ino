#include <PDM.h>

#define SAMPLE_RATE     16000       // 16 kHz - Frequência de amostragem do áudio
#define BUFFER_SIZE     512         // Tamanho do buffer - Array no qual os áudios serão alocados 

// Buffer para dados de áudio - Array onde os áudios serão alocados
int16_t sampleBuffer[BUFFER_SIZE];  // cada áudio terá o tamanho de 16bits

volatile int samplesRead = 0;

void onPDMdata() {
  int bytesAvailable = PDM.available();
  PDM.read(sampleBuffer, bytesAvailable);
  samplesRead = bytesAvailable / 2;
}

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("Iniciando captura de áudio...");

  // Configura o microfone PDM
  PDM.onReceive(onPDMdata);
  if (!PDM.begin(1, SAMPLE_RATE)) { // 1 canal, 16kHz
    Serial.println("Erro ao inicializar o microfone!");
    while (1);
  }

  Serial.println("Gravando áudio continuamente...");
  delay(1000); // Pequena espera antes de começar
}

void loop() {
  if (samplesRead > 0) {
    // Envia os dados como binário pela serial
    Serial.write((byte*)sampleBuffer, samplesRead * 2);
    samplesRead = 0;
  }
  // Aqui pode colocar um pequeno delay se quiser,
  // mas geralmente não é necessário para dados contínuos
}
