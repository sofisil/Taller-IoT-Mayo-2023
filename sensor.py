import Adafruit_DHT  # Libreria para uso de sensor
import RPi.GPIO as GPIO 
import time  

rojo = 16 # GPIO 16
amarillo = 20 # GPIO 20
verde = 21# GPIO 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(rojo , GPIO.OUT)
GPIO.setup(amarillo , GPIO.OUT) 
GPIO.setup(verde, GPIO.OUT) 

while True:
    sensor = Adafruit_DHT.DHT11 
    pin = 21 # Pin de conexion del sensor
    lectura = Adafruit_DHT.read_retry(sensor, pin)
    humedad = lectura[0]
    temperatura = lectura[1]
    print (type(lectura))
    print(humedad, temperatura)

    print ('Humedad: ' , humedad)
    print ('Temperatura: ' , temperatura)
    
    if temperatura> 28:
        GPIO.output(amarillo, GPIO.HIGH) 
        GPIO.output(verde, GPIO.LOW) 
        GPIO.output(rojo, GPIO.LOW) 

    elif temperatura <28:
        GPIO.output(amarillo, GPIO.LOW) 
        GPIO.output(verde, GPIO.LOW) 
        GPIO.output(rojo, GPIO.HIGH) 
    else:
        GPIO.output(amarillo, GPIO.LOW) 
        GPIO.output(verde, GPIO.HIGH) 
        GPIO.output(rojo, GPIO.LOW)
    
    time.sleep(5)  # pausa de 5 segunos 