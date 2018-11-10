import sensorcontrol as sc
import motorcontrol2 as mc
from time import sleep

s1
s2
s3
s4
s5
m11
m12
m21
m22

class Control
	def __init__(self):
		self.sensors=sc.Sensors(s1,s2,s3,s4,s5)
		self.motors=mc.MotorControl(m11,m12,m21,m22)

	def move(self, arr):
		index=0
		while 1: #index<len(arr)
			position=self.sensors.position()
			if position==10 || position =100:
				#self.motors.turnLeftHard  
				#T point array code here
				#check for end point
				self.motors.moveForward()
				sleep(.01)	#hard coded part here
				self.motors.stop()
				if(self.sensors.position()==100 || self.sensors.position()==10):		# assuming rectangular box at the end point
					break;
				else
					self.motors.moveBackward()
					sleep(.01)	#hard coded part here
					self.motors.stop()
					char=arr[index]
					if(char==F)
						self.motors.moveForward
					else if char==L
						while(self.sensors.position()!=0)
							self.motors.turnLeftHard()
						self.motors.stop()
						self.motors.moveForward()
					else if char==R
						while(self.sensors.position()!=0)
							self.motors.turnRightHard()
						self.motors.stop()
						self.motors.moveForward()
					
	
				#if end point then break
			else if position==2 :
				self.motors.turnLeftHard
			else if position==1 :
				self.motors.turnLeft
			else if position==0 :
				self.motors.moveForward
			else if position==-2 :
				self.motors.turnRightHard
			else if position==-1 s:
				self.motors.turnRight
			sleep(.01)
			self.motors.stop();
