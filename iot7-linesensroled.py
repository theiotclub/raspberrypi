from gpiozero import LineSensor,LED
from signal import pause

led = LED(12)
sensor = LineSensor(21)
sensor.when_line = led.on
sensor.when_no_line = led.off

pause()
