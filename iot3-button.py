from gpiozero import Button
from time import sleep
from signal import pause

button = Button(2)

button.when_pressed = lambda: print("Pressed")
button.when_released = lambda: print("Released")

pause()