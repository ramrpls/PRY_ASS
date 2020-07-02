import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from thinkdsp import read_wave


def Ploter(x):
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.35)
    t = np.arange(0.0, 1.0, 0.001)
    s = x
    l, = plt.plot(s)

    #Propiedades del [] en axSlider1, (izq->der) RelX,RelY,LargoDeSlider,AnchoDeSlider
    # axSlider1 = plt.axes([0.1,0.6,0.8,0.05])
    # sl1 = Slider(ax= axSlider1, label='Slider 1', valmin=0, valmax=9,valinit=0,valstep=1,closedmax=True,color='green')
    axDur = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')#eje Freq.
    sDur = Slider(ax=axDur, label='Duración', valmin=0,valmax=9, valinit=9, valstep=1)#Slider for Freq.
    axIni = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')#eje Amp.
    sIni = Slider(ax=axIni, label='Inicio', valmin=0,valmax=9, valinit=0, valstep=1)#Slider for Amp.


    def update(val):
        inicio = sIni.val #Almacena el valor seleccinado en el slider de Amp.
        dura = sDur.val #Almacena el valor seleccionado en el slider de Freq.
        plt.clf()
        newSeg = read_wave('outputRecording3.wav').segment(start=inicio,duration=dura).ys 
        Ploter(newSeg) #Re-asigna data en 'Y' con nueva Amp y Freq
        # plt.show() #Aparentemente re-dibuja la nueva figura en la misma ventana ploteada anteriormente

    sDur.on_changed(update)
    sIni.on_changed(update)

    # resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    # button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


    # def reset(event):
    #     sfreq.reset()
    #     samp.reset()
    # button.on_clicked(reset)
    plt.show()

Ploter(read_wave('outputRecording3.wav').segment(start=0,duration=9).ys)




#Adding new slider tests--------------(IT WORKS)
#Lectura y ploteo de imagen
# WaveIn = read_wave('outputRecording3.wav')
# WaveIn.plot(color='#ff6669')
# l, = plt.plot(plt.show(WaveIn.plot()))


#Propiedades del [] en axSlider1, (izq->der) RelX,RelY,LargoDeSlider,AnchoDeSlider
# axSlider1 = plt.axes([0.1,0.6,0.8,0.05])
# sl1 = Slider(ax= axSlider1, label='Slider 1', valmin=0, valmax=9,valinit=0,valstep=1,closedmax=True,color='green')






