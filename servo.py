import ssc32
import math
import time

ssc = ssc32.SSC32('/dev/ttyAMA0', 115200)

ssc[2].position = 1300
ssc[2].min = 600
ssc[2].max = 2400
ssc[2].deg_max = +90.0
ssc[2].deg_min = -90.0
ssc[2].degrees = -45.0

ssc.showversion()
ssc.commit(time=2000)
while not ssc.is_done():
	time.sleep(0.1)
	
ssc[2].degrees = 0
ssc.commit(time=2000)
#ssc[2].degrees = 45.0
