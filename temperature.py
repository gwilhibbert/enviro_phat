import os
import time
from envirophat import light, motion, weather, leds
from datetime import datetime

out = open('temp2.log', 'w')
out.write('time\ttemperature\n')
#choice=input("how many hours do you want to run")
run_time=3600*24#int(choice)
start_time=time.time()
current_time=start_time

try:
    while current_time<=(start_time+run_time):
        temp = weather.temperature()
        out.write(str(datetime.now())+"\t"+str(temp)+"\n")
        out.flush()
        os.fsync(out)
        current_time=time.time()
        time.sleep(10)

except KeyboardInterrupt:
    leds.off()
    out.close()
