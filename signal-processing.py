from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
t = [-3, 1, 2, -2, 3, -1]
ax.plot(t,'o-')
ax.set_xlabel('Time',fontsize=18)
ax.set_ylabel('Amplitude',fontsize=18)

substracted = [2 - i for i in t]

ax.plot(substracted,'o-')
ax.set_xlabel('Time',fontsize=18)
ax.set_ylabel('Amplitude',fontsize=18)

twoThirds = [(i / 3) * 2 + 1 for i in t]

ax.plot(twoThirds,'o-')
ax.set_xlabel('Time',fontsize=18)
ax.set_ylabel('Amplitude',fontsize=18)

power = [i*i for i in t]

ax.plot(power,'o-')
ax.set_xlabel('Time',fontsize=18)
ax.set_ylabel('Amplitude',fontsize=18)

twoToPowerI = [2**i for i in t]

ax.plot(twoToPowerI,'o-')
ax.set_xlabel('Time',fontsize=18)
ax.set_ylabel('Amplitude',fontsize=18)

messedUp = [(2**i) - (i**3) for i in t]

ax.plot(messedUp,'o-')
ax.set_xlabel('Time',fontsize=18)
ax.set_ylabel('Amplitude',fontsize=18)

plt.show()