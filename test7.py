import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from thinkdsp import read_wave


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
t = np.arange(0.0, 1.0, 0.001)
s = read_wave('outputRecording3.wav').ys
l, = plt.plot(s)


axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)#eje Freq.
sfreq = Slider(axfreq, 'Duración', 0.01, 9, valinit=9)#Slider for Freq.
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)#eje Amp.
samp = Slider(axamp, 'Inicio', 0.01, 9, valinit=0)#Slider for Amp.


# def update(val):
#     amp = samp.val #Almacena el valor seleccinado en el slider de Amp.
#     freq = sfreq.val #Almacena el valor seleccionado en el slider de Freq.
#     plt.clf()
#     segment = WaveIn.segment(start=amp, duration=freq)
#     segment.plot(color='#66a3ff')
#     plt.xlabel('Tiempo (s)')
#     plt.title('Onda #3')
#     plt.grid(True)
#     # l.set_ydata(segment) #Re-asigna data en 'Y' con nueva Amp y Freq
#     fig.canvas.draw_idle() #Aparentemente re-dibuja la nueva figura en la misma ventana ploteada anteriormente

# sfreq.on_changed(update)
# samp.on_changed(update)

# resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


# def reset(event):
#     sfreq.reset()
#     samp.reset()
# button.on_clicked(reset)






#Adding new slider tests--------------(IT WORKS)
#Lectura y ploteo de imagen
# WaveIn = read_wave('outputRecording3.wav')
# WaveIn.plot(color='#ff6669')
# l, = plt.plot(plt.show(WaveIn.plot()))


#Propiedades del [] en axSlider1, (izq->der) RelX,RelY,LargoDeSlider,AnchoDeSlider
# axSlider1 = plt.axes([0.1,0.6,0.8,0.05])
# sl1 = Slider(ax= axSlider1, label='Slider 1', valmin=0, valmax=9,valinit=0,valstep=1,closedmax=True,color='green')






plt.show()