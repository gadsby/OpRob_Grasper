from Servo import *
import math
import time

dyn = USB2Dynamixel_Device('/dev/tty.usbserial-AH01FOYT')
serv = Robotis_Servo( dyn, 1, "MX")

serv.move_angle(math.radians(75))
print serv.read_load()
serv.move_angle(math.radians(75.1))
print serv.read_load()
serv.move_angle(math.radians(75.2))
print serv.read_load()
serv.move_angle(math.radians(75.3))
print serv.read_load()
serv.move_angle(math.radians(75.4))
print serv.read_load()
serv.move_angle(math.radians(75.5))
print serv.read_load()
serv.move_angle(math.radians(60))



#serv.init_cont_turn()
#serv.set_angvel(math.radians(30))#

#time.sleep(5)
#serv.kill_cont_turn()