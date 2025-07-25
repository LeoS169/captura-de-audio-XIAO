# captura-de-audio-XIAO

### Esse repositório apresenta uma forma simples de capturar áudio através da placa de desenvolvimento Seeed Xiao Ble Sense que usa o microcontrolador nRF52840, usando o Python.



A Placa de desevolvimento Xiao Ble Sense é um dispositivo fabricado pela Seeed Studio que porta como hardware o microcontrolador **nRF 52840** e um microfone digital com modulação de densidade de pulso, ou simplismente PDM.
<div style="text-align: center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGkku2nEQdIFBsEjCudaibNdMYmN8gsUwEcw&s">
</div>



Para mais informações e configurações iniciais da XIAO, seguir o tópico ***Getting Started***, no site da [Documentação da xiao](https://wiki.seeedstudio.com/XIAO_BLE/).

## Dependências
Para a XIAO:

    - Biblioteca PDM

Para o Python:
    
    Bibliotecas
    - serial
    - wave
    - time
    - numpy

## Captura:
Para efetuar a captura de áudio usando o microfone da **XIAO BLE SENSE**, seguir os passos:

- Conectar XIAO BLE SENSE ao computador
- Abrir arquivo *envia_audio_serial.ino* no Arduino IDE
- Instalar dependências necessárias
- Escolher a placa XIAO nRF52840 entre as placas disponíveis (de acordo com site da Xiao Ble Sense)
- Clicar em ENVIAR para compilar e enviar o código para a placa
- Após termino, conferir saída no serial (a saída deverá ser composta por caracteres e mudar conforme algum som seja captado)

Feito isso, abrir pasta com código python através da IDE da sua preferência. Então, seguir os passos:
- Instalar a biblioteca serial
```
pip install serial wave numpy
```
- Abrir arquivo gravacao.py
- Definir duração de gravação do áudio em (definido em segundos)
```
DURATION = x 
```
- Definir o local onde o arquivo será criado na linha
```
with open("<local em que será salvo>", "wb") as wf:...
```
- Rodar o código.

Ao fim do tempo definido, o arquivo será salvo no formato .wav


## Como funciona?
> 1 - Inicialmente, o código *envia_audio_serial.ino* faz com que os dados do microfone sejam enviados para a porta serial COM9 bit a bit. Ao abrir o o Monitor Serial no Arduino IDE é possível visualizar a representação gráfica do áudio gravado.

> 2 - Após isso, se CERTIFICAR que o Monitor Serial esteja fechado, pois ele utiliza a porta COM9 para imprimir os dados e a porta precisa estar livre para que a conexão com o script Python, que usará a porta seral, aconteça sem erros.

> 3 - Enfim, ao rodar o script Python, ele irá se conectar com a porta COM9 e irá ler os dados enviados pela placa XIAO no intervalo definido em DURACAO, convertendo então os dados binários em um arquivo .wav no local destinado pelo usuário.