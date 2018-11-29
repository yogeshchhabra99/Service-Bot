#import positiondetect
#pos=positiondetect.position()
#print pos

#arr = ['S','L','L','R']
arr = ['R','S']
import motioncontrol2 as cont
controller=cont.Control()
controller.move(arr)
