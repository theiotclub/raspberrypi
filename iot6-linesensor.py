from gpiozero import LineSensor
from signal import pause

sensor = LineSensor(21)
sensor.when_line = lambda: print('Object Detected')
sensor.when_no_line = lambda:print('Object Not Detected')

pause()