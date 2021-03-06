# uau.e
Robô com expressoes.

Um robô controlado por celular via aplicativo blynk, que mostrará expressões pré-escolhidas em uma tela OLED 0.96" SSD1306 , usando Node MCU ESP8266 para receber e processar os dados.

## Materiais:

•	NodeMCU ESP8266

•	Motores DC 5V

•	Driver motor ponte H L298N

•	Display oLED 0.96” SSD1306

•	Cabos jumper

NodeMCU: O módulo Wifi ESP8266 NodeMCU é uma placa de desenvolvimento que combina o chip ESP8266, uma interface usb-serial e um regulador de tensão 3.3V. A linguagem de programação será MicroPython.

Driver motor ponte H: possui dois canais e permite controlar velocidade e sentido de rotação de até dois motores ao mesmo tempo.

Display oLED: display gráfico de alto contraste com resolução de 128x64.
Possui uma memoria interna de 1KB organizada em 8 linhas com 128 segmentos em cada, podendo guardar 8 bits de dados por segmento.

 

|Características               |Parâmetros|
|---|---|
|Tecnologia do Display         | OLED  |
|Interface MCU                 | I2C / SPI  | 
|Tamanho da tela               | 0.96 polegadas  |
|Resolução                     |128×64 pixels|
|Tensão de operação            |3.3V – 5V|
|Corrente de operação          |20mA max|
|Angulo de visão               |160°|
|Caracteres por linha          |21 |
|Numero de linhas de caracteres|7|
|memória                       |1KB|

<img src="https://www.ckn.io/images/13-oled-1.png" width="500" height="300">

## OLED Pinout
GND - pino do terra 0v

VCC - entrada de tensão min 3.3v

SCL - pino de clock serial para interface I2C

SDA - pino de dados serial para interface I2C

## Blynk

Projeto do controle do robô criado no app Blynk

<img src="Screenshot_20191202-115910[1].jpg" width="300" height="500">

Configuração dos botões 

<img src="Screenshot_20191202-115940[1].jpg" width="300" height="500">

Configuração do menu

<img src="Screenshot_20191202-115954[1].jpg" width="300" height="500">

Configuração da placa e do token

<img src="Screenshot_20191202-115929[1].jpg" width="300" height="500">

## Montagem do Circuito

<img src="Circuito UAU.e.PNG" width="600" height="500">

## Montagem do Robô

<img src="IMG_20191130_145302617.jpg" width="500" height="400">
<img src="IMG_20191130_145245673.jpg" width="500" heigth+"400">



Video do funcionamento:
https://youtu.be/iXfSD9A_K8w
