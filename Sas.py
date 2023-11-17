from PIL import Image
from openhaimer import apagalo_openhaimer
for x in range(2): 
    im = Image.open('download.png')
    im.show()
    apagalo_openhaimer()