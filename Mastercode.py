


from machine import Pin, I2C, Timer
from time import sleep
import time
import ssd1306
import framebuf
import urequests as requests
import network

tim = Timer(-1)

ligado = 0
desligado = 1

in1 = Pin(14, Pin.OUT)
in2 = Pin(12, Pin.OUT)
in3 = Pin(13, Pin.OUT)
in4 = Pin(15, Pin.OUT)

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

def read(t):
  value = requests.get("http://blynk-cloud.com/iTArttJxBXtIN76gIDHXx-pHJP3-Xapx/get/v0")
  value = int(value.text[2])
  
  botao = requests.get("http://blynk-cloud.com/iTArttJxBXtIN76gIDHXx-pHJP3-Xapx/get/v1")
  botao = int(botao.text[2])
  
  image(value)
  motor(botao)

def image(img):
  if img==1:
    oLED("image.pbm")
  elif img==2:
    oLED("image3.pbm")
  elif img==3:
    oLED("image2.pbm")

def oLED(file):
  with open(file, 'rb') as f:
    f.readline()
    f.readline()
    f.readline()
    data = bytearray(f.read())
  fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
  display.invert(1)
  display.blit(fbuf, 0, 0)
  display.show()
  
def motor(direcao):
  if direcao==3:
    in1.value(desligado)
    in2.value(ligado)
    in3.value(ligado)
    in4.value(desligado)
  
  elif direcao==1:
    in1.value(ligado)
    in2.value(desligado)
    in3.value(desligado)
    in4.value(ligado)
  
  elif direcao==4:
    in1.value(ligado)
    in2.value(desligado)
    in3.value(ligado)
    in4.value(desligado)
 
  elif direcao==2:
    in1.value(desligado)
    in2.value(ligado)
    in3.value(desligado)
    in4.value(ligado)
  
  else:
    in1.value(desligado)
    in2.value(desligado)
    in3.value(desligado)
    in4.value(desligado)


tim.init(period=100,mode=Timer.PERIODIC,callback=read)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.connect('Igorrrrr', '31415igor')

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP-AP')

sleep(2)

