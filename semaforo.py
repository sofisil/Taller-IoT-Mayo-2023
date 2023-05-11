import RPi.GPIO as GPIO # Libreria para manejo de pines 
import time

# Los Pines de conexion GPIO 16, GPIO 20, GPIO 21
rojo = 16
amarillo = 20
verde = 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(rojo , GPIO.OUT)
GPIO.setup(amarillo , GPIO.OUT) 
GPIO.setup(verde, GPIO.OUT) 

#Led Rojo
GPIO.output(rojo, GPIO.HIGH)
time.sleep(3)
GPIO.output(rojo, GPIO.LOW)