import sensorcontrol as sc
import motorcontrol2 as mc
from time import sleep

s1=3
s2=5
s3=7
s4=11	#near=12
s5=13
m11=29
m12=33
m21=35
m22=37


class Control:
	def __init__(self):
		self.sensors=sc.Sensors(s1,s2,s3,s4,s5)
		self.motors=mc.MotorControl(m11,m12,m21,m22)
	#main function
	def __del__(self):
		self.motors.stop()
		#delete self.motors()
	def move(self, arr):
		index=0
		while 1: #index<len(arr)
			position=self.sensors.position()
			print "arr:" 
			print arr
			print "position:"+str(position)
			if position==10 or position ==100:
				sleep(0.2)
				if self.sensors.position()!=10 and self.sensors.position()!=100:
					continue
		
				#self.motors.turnLeftHard  
				#T point array code here
				#check for end point
			#1st method	#self.motors.moveForward()
			#	sleep(.1)	#hard coded part here
			#	self.motors.stop()
			#	if self.sensors.position()==10 or self.sensors.position()==100 :		# assuming rectangular box at the end point
			#		break;
			#	else:
			#		self.motors.moveBackward()
			#		sleep(.01)	#hard coded part here		#second method
				if index>=len(arr):
					break
				else:
					self.motors.moveForward()
					sleep(1)
					self.motors.stop()
					sleep(0.1)
					char=arr[index]
					index=index+1
					if(char=='S'):
						while self.sensors.position()!=0 :	
							self.motors.moveForward()
						self.motors.stop()
						self.motors.moveForward()
					elif char=='L':
						while self.sensors.position()!=0 and self.sensors.position()!=1 :
							self.motors.turnLeftHard()
							sleep(0.1)
							self.motors.stop()
							sleep(0.1)
						self.motors.stop()
						self.motors.moveForward()
					elif char=='R':
						while self.sensors.position()!=0 :
							self.motors.turnRightHard()
						self.motors.stop()
						self.motors.moveForward()
					
	
				#if end point then break
			elif position==2 :
				self.motors.moveForward()
				sleep(0.5)
				self.motors.stop()
				sleep(0.1)
				self.motors.turnLeftHard()
				while self.sensors.position()!=0 :
					print "turning"
				self.motors.stop()
			elif position==1 :
				self.motors.turnLeft()
			elif position==0 :
				self.motors.moveForward()
			elif position==-2 :
				self.motors.turnRightHard()
			elif position==-1 :
				self.motors.turnRight()
			sleep(.1)
			self.motors.stop();
