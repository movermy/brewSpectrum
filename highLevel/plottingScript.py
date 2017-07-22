#some attempts to learn plotting with python
#ideally, this will feed into the ability
#to make a scrolling plot


#modified from: https://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
import numpy as np
import matplotlib.pyplot as plt


plt.ion()

for i in range(1000):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

    minX = max(0, i-10)

    plt.axis([minX, i+1, 0, 1])

while True:
    plt.pause(0.05)



