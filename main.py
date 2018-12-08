#import positiondetect
#pos=positiondetect.position()
#print pos

#arr = ['S','L','L','R']
arr = ['R','L']
import motioncontrol2 as cont
controller=cont.Control()
#controller.takeUTurn()
controller.move(arr)
