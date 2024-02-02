# from pylab import *
from widgets import Slider, Button
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.45)
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*t)
c = np.cos(2*np.pi*t)
sl, = plt.plot(t,s, lw=2, c='g')
cl, = plt.plot(t,c, lw=2, c='r')
plt.axis([0, 1, -10, 10])

axcolor = 'lightgoldenrodyellow'
axfreqs = plt.axes([0.125, 0.1, 0.775, 0.03])#, axisbg=axcolor)
axamps  = plt.axes([0.125, 0.15, 0.775, 0.03])#, axisbg=axcolor)
axfreqc = plt.axes([0.125, 0.2, 0.775, 0.03])#, axisbg=axcolor)
axampc  = plt.axes([0.125, 0.25, 0.775, 0.03])#, axisbg=axcolor)

sfreqs = Slider(axfreqs, 'Freq sine', 0.1, 30.0, valinit=1)
                # works like before
samps = Slider(axamps, 'Amp sine', 0.1, 10.0, valinit=2,
               update_func_only_on_release_event=True)
                # Here the slider is moving but the data is updated only after
                # the release.
sfreqc = Slider(axfreqc, 'Freq cosine', 0.1, 30.0, valinit=1,
                dragging=False)
                # works like before
sampc = Slider(axampc, 'Amp cosine', 0.1, 10.0, valinit=1,
               dragging=False, update_func_only_on_release_event=True)
                # Internally update_func_only_on_release_event is set False
                #   (if not: The change would be shown after the release.
                #    But nobody wants this if dragging = False!)
                # So in the end: Tt works like before.


def update(val):
    amp = samps.val
    freq = sfreqs.val
    sl.set_ydata(amp*np.sin(2*np.pi*freq*t))
    amp = sampc.val
    freq = sfreqc.val
    cl.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw()

sfreqs.on_changed(update)
samps.on_changed(update)
sfreqc.on_changed(update)
sampc.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset')

def reset(event):
    sfreqs.reset()
    samps.reset()
    sfreqc.reset()
    sampc.reset()
button.on_clicked(reset)
    

plt.show()

