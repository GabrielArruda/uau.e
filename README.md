# uau.e
Robô com expressoes.

Um robô controlado por celular via aplicativo blynk, que mostrará expressões pré-escolhidas em uma tela oLED 0.96", usando Node MCU ESP8266 para receber e processar os dados.

Materiais:

•	NodeMCU ESP8266

•	Conversor nível lógico

•	Motores DC 5V

•	Driver motor ponte H L298N

•	Display oLED 0.96”

•	Jumper

NodeMCU: O módulo Wifi ESP8266 NodeMCU é uma placa de desenvolvimento que combina o chip ESP8266, uma interface usb-serial e um regulador de tensão 3.3V. A linguagem de programação será MicroPython.

Conversor nível lógico: converte o sinal de 3.3V para 5V, assim gerando a comunicação entre o NodeMCU e o driver motor ponte H.

Driver motor ponte H: possui dois canais e permite controlar velocidade e sentido de rotação de até dois motores ao mesmo tempo.

Display oLED: display gráfico de alto contraste com resolução de 128x64.
