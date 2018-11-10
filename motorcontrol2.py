import Rpi.GPIO as GPIO


class MotorControl:
	def __init__(self,motor1Pin1,motor1Pin2,motor2Pin1,motor2Pin2):
		#self.motor1=Motor(forward=motor1Pin1,backward=motor1Pin2)
		#self.motor2=Motor(forward=motor2Pin1,backward=motor2Pin2)
		GPIO.setMode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.motor1Pin1,GPIO.OUT)	#eg 11,12,15,16
		GPIO.setup(self.motor1Pin2,GPIO.OUT)
		GPIO.setup(self.motor2Pin1,GPIO.OUT)
		GPIO.setup(self.motor2Pin2,GPIO.OUT)

	def moveForward(self):
		GPIO.output(self.motor1Pin1,GPIO.HIGH)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.HIGH)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
	
	def moveBackward(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.HIGH)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.HIGH)

	def stop(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
	
	def turnLeft(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.HIGH)
		GPIO.output(self.motor2Pin2,GPIO.LOW)

	def turnReft(self):
		GPIO.output(self.motor1Pin1,GPIO.HIGH)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.LOW)

	def turnLeftHard(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.HIGH)
		GPIO.output(self.motor2Pin1,GPIO.HIGH)
		GPIO.output(self.motor2Pin2,GPIO.LOW)

	def turnReftHard(self):
		GPIO.output(self.motor1Pin1,GPIO.HIGH)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.HIGH)
