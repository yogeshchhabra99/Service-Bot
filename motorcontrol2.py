import RPi.GPIO as GPIO


class MotorControl:
	def __init__(self,motor1Pin1,motor1Pin2,motor2Pin1,motor2Pin2,motor1Pin1_,motor1Pin2_,motor2Pin1_,motor2Pin2_):
		#self.motor1=Motor(forward=motor1Pin1,backward=motor1Pin2)
		#self.motor2=Motor(forward=motor2Pin1,backward=motor2Pin2)
		
		self.motor1Pin1=motor1Pin1	#eg 11,12,15,16
		self.motor1Pin2=motor1Pin2
		self.motor2Pin1=motor2Pin1
		self.motor2Pin2=motor2Pin2
		self.motor1Pin1_=motor1Pin1_	#eg 11,12,15,16
		self.motor1Pin2_=motor1Pin2_
		self.motor2Pin1_=motor2Pin1_
		self.motor2Pin2_=motor2Pin2_

		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.motor1Pin1,GPIO.OUT)	#eg 11,12,15,16
		GPIO.setup(self.motor1Pin2,GPIO.OUT)
		GPIO.setup(self.motor2Pin1,GPIO.OUT)
		GPIO.setup(self.motor2Pin2,GPIO.OUT)
		GPIO.setup(self.motor1Pin1_,GPIO.OUT)	#eg 11,12,15,16
		GPIO.setup(self.motor1Pin2_,GPIO.OUT)
		GPIO.setup(self.motor2Pin1_,GPIO.OUT)
		GPIO.setup(self.motor2Pin2_,GPIO.OUT)

	def moveForward(self):
		GPIO.output(self.motor1Pin1,GPIO.HIGH)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.HIGH)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
		GPIO.output(self.motor1Pin1_,GPIO.HIGH)
		GPIO.output(self.motor1Pin2_,GPIO.LOW)
		GPIO.output(self.motor2Pin1_,GPIO.HIGH)
		GPIO.output(self.motor2Pin2_,GPIO.LOW)
	

	def moveBackward(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.HIGH)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.HIGH)
		GPIO.output(self.motor1Pin1_,GPIO.LOW)
		GPIO.output(self.motor1Pin2_,GPIO.HIGH)
		GPIO.output(self.motor2Pin1_,GPIO.LOW)
		GPIO.output(self.motor2Pin2_,GPIO.HIGH)

	def stop(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
		GPIO.output(self.motor1Pin1_,GPIO.LOW)
		GPIO.output(self.motor1Pin2_,GPIO.LOW)
		GPIO.output(self.motor2Pin1_,GPIO.LOW)
		GPIO.output(self.motor2Pin2_,GPIO.LOW)
	
	def turnLeft(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.HIGH)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
		GPIO.output(self.motor1Pin1_,GPIO.LOW)
		GPIO.output(self.motor1Pin2_,GPIO.LOW)
		GPIO.output(self.motor2Pin1_,GPIO.HIGH)
		GPIO.output(self.motor2Pin2_,GPIO.LOW)

	def turnRight(self):
		GPIO.output(self.motor1Pin1,GPIO.HIGH)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
		GPIO.output(self.motor1Pin1_,GPIO.HIGH)
		GPIO.output(self.motor1Pin2_,GPIO.LOW)
		GPIO.output(self.motor2Pin1_,GPIO.LOW)
		GPIO.output(self.motor2Pin2_,GPIO.LOW)

	def turnLeftHard(self):
		GPIO.output(self.motor1Pin1,GPIO.LOW)
		GPIO.output(self.motor1Pin2,GPIO.HIGH)
		GPIO.output(self.motor2Pin1,GPIO.HIGH)
		GPIO.output(self.motor2Pin2,GPIO.LOW)
		GPIO.output(self.motor1Pin1_,GPIO.LOW)
		GPIO.output(self.motor1Pin2_,GPIO.HIGH)
		GPIO.output(self.motor2Pin1_,GPIO.HIGH)
		GPIO.output(self.motor2Pin2_,GPIO.LOW)

	def turnRightHard(self):
		GPIO.output(self.motor1Pin1,GPIO.HIGH)
		GPIO.output(self.motor1Pin2,GPIO.LOW)
		GPIO.output(self.motor2Pin1,GPIO.LOW)
		GPIO.output(self.motor2Pin2,GPIO.HIGH)
		GPIO.output(self.motor1Pin1_,GPIO.HIGH)
		GPIO.output(self.motor1Pin2_,GPIO.LOW)
		GPIO.output(self.motor2Pin1_,GPIO.LOW)
		GPIO.output(self.motor2Pin2_,GPIO.HIGH)



