import time
from envirophat import light, motion, weather, leds

out = open('enviro.log', 'w')
out.write('light\trgb\tmotion\theading\ttemp\tpress\n')
run_time=60
start_time=time.time()
input("light level")
print(light.light())
input("lights will go on")
leds.on()
print("lights on")
input("lights will go off")
leds.off()
print("LEDs off")
input("rgb values next")
print(str(light.rgb())[1:-1].replace(' ', ''))
input("accelermoneter reading next")
print(str(motion.accelerometer())[1:-1].replace(' ', ''))
input("accelermoneter reading next")
print(str(motion.accelerometer())[1:-1].replace(' ', ''))
input("accelermoneter reading next")
print(str(motion.accelerometer())[1:-1].replace(' ', ''))
input("heading next")
print(motion.heading())
input("heading next")
print(motion.heading())
input("heading next")
print(motion.heading())
input("temperature next")
print(weather.temperature())
input("weather pressure next")
print(weather.pressure())


current_time=start_time

try:
    while current_time<=(start_time+run+time):
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        out.write('%f\t%s\t%s\t%f\t%f\t%f\n' % (lux, rgb, acc, heading, temp, press))
        current_time=time.time()
        time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    out.close()
