from gpiozero import Robot, LineSensor
from signal import pause

robot = Robot(left=(6, 13), right=(21, 20))
left_sensor = LineSensor(4)
right_sensor= LineSensor(26)

robot.forward(0.4)

def movfront():
        robot.forward(0.4)

def leftmove():
        robot.left(0.3)

def rightmove():
        robot.right(0.3)


left_sensor.when_line = leftmove
right_sensor.when_line = rightmove

left_sensor.when_no_line = movfront
right_sensor.when_no_line = movfront

pause()
