import RPi.GPIO as GPIO, GPIO1
import time

PIR_GPIO_PIN=19
RELAY_GPIO_PIN=23

GPIO.setmode(GPIO.BCM)
GPIO1.setmode(GPIO.BCM)

GPIO.setup(PIR_GPIO_PIN,GPIO.IN)
GPIO1.setup(RELAY_GPIO_PIN,GPIO.OUT)
GPIO1.output(RELAY_GPIO_PIN,GPIO.LOW)
print("Motion dependent security sensor")
time.sleep(2)

while True:
    if GPIO.input(PIR_GPIO_PIN):
        print("Motion detected")
        GPIO1.output(RELAY_GPIO_PIN, GPIO.HIGH)
        