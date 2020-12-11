from gpiozero import LightSensor

sensor = LightSensor(4)

while True:
    sensor.wait_for_light()
    print("Its light")
    sensor.wait_for_dark()
    print("Its dark")
    
