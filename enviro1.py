import time
from envirophat import light, motion, weather, leds


  
try:
    while True:
        which=int(input("enter follwing numbers for following functions \n1 led on\n2 led off\n3 measure light\n4 measure rgb levels\n5 measure acceleration\n6 measure heading\n7 measure temperature\n8 measure pressure\n"))
        if which==1:
            leds.on()
        elif which==2:
            leds.off()
        elif which ==3:
            print(light.light())
        elif which==4:
            print(str(light.rgb())[1:-1].replace(' ', ''))
        elif which==5:
            print(str(motion.accelerometer())[1:-1].replace(' ', ''))
        elif which==6:
            print(motion.heading())
        elif which==7:
            print(weather.temperature())
        elif which==8:
            print(weather.pressure())
        else:
            print("incorrect selection")
        time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    out.close()
