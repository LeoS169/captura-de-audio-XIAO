import serial
import wave
import time
import numpy as np

# Configurações
PORT = 'COM9'          # Ajuste para sua porta serial
BAUDRATE = 115200       # Taxa de transmissão de dados na serial. 115200 bits por segundo 
SAMPLE_RATE = 16000     # Hz Taxa de amostragem 
CHANNELS = 1            # Canais de audio (1 - mono)
SAMPLE_WIDTH = 2        # tamanho de cada amostragem em bytes (16 bits)
DURATION = 60       # Duração da gravação
BUFFER_SIZE = 512       # Quantidade de amostras por bloco de leitura       
# igual ao buffer da placa (em samples)

def main():
    ser = serial.Serial(PORT, BAUDRATE, timeout=1) # Se comunica com o serial

    num_samples_total = SAMPLE_RATE * DURATION
    num_bytes_total = num_samples_total * SAMPLE_WIDTH

    print(f"Iniciando gravação de {DURATION} segundos...")

    frames = bytearray()

    start_time = time.time()
    while len(frames) < num_bytes_total:
        if ser.in_waiting > 0:
            data = ser.read(BUFFER_SIZE * SAMPLE_WIDTH)
            frames.extend(data)

    ser.close()
    print("Gravação concluída!")

    # Salva em arquivo WAV
    with wave.open("arquivos_audio/verde/verde10.wav", "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(SAMPLE_WIDTH)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(frames)

    print("Arquivo gravacao.wav salvo!")

if __name__ == "__main__":
    main()
