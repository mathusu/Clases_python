import sys #Prueba de como funcionan el importar un archivo como libreria
import time
from playsound import playsound
from PIL import Image
import tkinter

def apagalo_openhaimer():

    im = Image.open('download.png')
    im.show()

    playsound('Sonido gracioso.wav')

apagalo_openhaimer()