# captura-de-audio-XIAO

Esse repositório apresenta uma forma simples de capturar áudio através da placa de desenvolvimento Seeed Xiao Ble Sense, usando o Python.



A Placa de desevolvimento Xiao Ble Sense é um dispositivo fabricado pela Seeed Studio que porta como hardware o microcontrolador **nRF 52840** e um microfone digital com modulação de densidade de pulso, ou simplismente PDM.
<div style="text-align: center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGkku2nEQdIFBsEjCudaibNdMYmN8gsUwEcw&s">
</div>


Para configurações iniciais da XIAO, seguir o tópico ***Getting Started***, no site da [Documentação da xiao](https://wiki.seeedstudio.com/XIAO_BLE/).

## Captura:
Para efetuar a captura de áudio usando o microfone da **XIAO BLE SENSE**, seguir os passos:

- Conectar XIAO BLE SENSE ao computador
- Abrir arquivo *envia_audio_serial.ino* no Arduino IDE
- Escolher a placa XIAO nRF52840 entre as placas disponíveis
- Clicar em ENVIAR para compilar e enviar o código para a placa
- Após termino, conferir saída no serial (a saída deverá ser composta por caracteres e mudar conforme algum som seja captado)

Feito isso, abrir pasta com código python através da IDE da sua preferência. Então, seguir os passos:
- Instalar a biblioteca serial
```
pip install serial
```
- Abrir arquivo gravacao.py
- Definir tempo de escolha em
```
DURATION = x #em segundos
```
- Definir o local onde o arquivo será criado na linha
```
with open("<local em que será salvo>", "wb") as wf:...
```
- Rodar o código.

Ao fim do tempo definido, o arquivo será salvo no formato .wav

