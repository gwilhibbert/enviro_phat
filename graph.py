import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime
import matplotlib.dates as mdates


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animate(i):
    while True:
        filename="temp.log"#input("filename?")
        try:
            graph_data=open(filename,"r").read()
            break
        except:
            print("invalid filename")
    
    lines = graph_data.split('\n')
    lines=lines[1:]
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            items = line.split()
            #print(items)
            x=items[0][5:]+" "+items[1]
            y=items[2]
            #x=x.split(".")[0]
            x=datetime.strptime(x,"%m-%d %H:%M:%S.%f")
            #x = matplotlib.dates.date2num(x)
            xs.append((x))
            ys.append(float(y)-6.0)
    ax.clear()
    ax.plot(xs, ys)
    ax.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax.yaxis.set_major_locator(plt.MaxNLocator(10))
    xformatter = mdates.DateFormatter('%H:%M')
    plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

