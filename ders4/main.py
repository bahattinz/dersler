from custom_thread import *
import time
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def start_thread():
    for i in range(5):
        t=CustomThread(title="Thread_{}".format(i+1),time=i+1)
        t.start()

def get_value(link):
    t=CustomThread2(link=link)
    t.start()

fig = plt.figure()
graph = fig.add_subplot(111)
current_axis = plt.gca()
current_axis.set_ylim([4,5])
labels = current_axis.get_xticklabels()
plt.setp(labels, rotation=90)
graph.grid(True)

def show_data(i):
    print("refreshing..")
    current_folder = os.path.dirname(__file__)
    # data = np.genfromtxt(os.path.join(current_folder,"dolar.csv"))
    data = pd.read_csv(os.path.join(current_folder,"dolar.csv"))
    graph.plot(data["time"], data["value"],c="red")
    # plt.show()

def show_animation():
    get_value("https://tr.investing.com/currencies/usd-try")
    ani = animation.FuncAnimation(fig, show_data, interval=1000)
    plt.show()

# get_value("https://tr.investing.com/currencies/usd-try")
# get_value("https://tr.investing.com/currencies/eur-try")

# show_data()
show_animation()
print("İŞLEM TAMAMLANDI!")
