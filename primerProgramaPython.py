#tipos de datos:
#strings: "texto"
#int 4
#float 4.5
#bool True False

#Apente de Programación orientada a objetos
def funcion ():
    contenido=0
    return 0
class Personas:
    #metodo constructor 
    #sirve para construir objetos con propiedades iniciales
    def __init__(self,extremidades,cabeza,nombre,raciocinio,parado,velocidad,color):
        self.var_extremidades=extremidades
        self.var_cabeza=cabeza
        self.var_nombre=nombre
        self.var_raciocinio=raciocinio
        self.var_parado=parado
        self.var_velocidad=velocidad
        self.var_color=color
        
    #metodo
    def caminar(self):
        self.var_parado=False
        self.var_velocidad=5
        print("esta persona tiene %s extremidades y es de color %s "%(self.var_extremidades,self.var_color))
        print(self.var_nombre, "está caminando y va a la velocidad de: ", self.var_velocidad)
    def sentar(self):
        animacion=0
        return animacion
    def estudiarPython(self):
        self.var_raciocinio=100000

Alien=Personas(4,2,"Gerardo",12343242,True,0,"verde")
Alien.caminar()











