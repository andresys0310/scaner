import os
class Informacion:
    def obtenerInfo(self):
        comando='ipconfig'
        tubo=os.popen(comando)
        datos=tubo.readlines()
        print(datos[13])


i=Informacion()
i.obtenerInfo()

        
