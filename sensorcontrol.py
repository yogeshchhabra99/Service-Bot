import Rpi.GPIO as GPIO


class Sensors:
	def __init__(self,s1,s2,s3,s4,s5):
		#self.motor1=Motor(forward=motor1Pin1,backward=motor1Pin2)
		#self.motor2=Motor(forward=motor2Pin1,backward=motor2Pin2)
		GPIO.setMode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(s1,GPIO.IN)
		GPIO.setup(s2,GPIO.IN)
		GPIO.setup(s3,GPIO.IN)
		GPIO.setup(s4,GPIO.IN)
		GPIO.setup(s5,GPIO.IN)
		
	def position(self):
		m1=GPIO.input(s1)
		m2=GPIO.input(s2)
		m3=GPIO.input(s3)
		m4=GPIO.input(s4)
		m5=GPIO.input(s5)
		
		if m1==1 and m4==1 and m2==1 and m3==1 and m5==1:	#T point
			return 100
		
		if m4==1 and m2==1 and m3==1 :	#T point
			return 10
		if m2==1 :
			return 1
		if m1==1 :
			return 2
		if m4==1 :
			return -1
		if m5==1 :
			return -2
		if m3==1 :
			return 0
		else:
			return 20
	

