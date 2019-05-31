import time
from envirophat import light, motion, weather, leds

out = open('enviro.log', 'w')
out.write('motion\n')
run_time=60
start_time=time.time()
current_time=start_time

try:
    while current_time<=(start_time+run+time):
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        out.write('%f\n' % (acc))
        current_time=time.time()
        time.sleep(0.1)

except KeyboardInterrupt:
    leds.off()
    out.close()
