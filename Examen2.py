from abc import(ABC, abstractmethod)

class Documentos(ABC):

    __fechadedefuncion = 0
    __fechadenacimiento = 0

    def __init__(self, numerodelibro, numerodefolio, fechaderegistro):
        if fechaderegistro < 2001:

            self.numerodelibro = numerodelibro
            self.numerodefolio = numerodefolio
            self.fechaderegistro = fechaderegistro

        else:

            print("Los documentos posteriores al año 2001 no son incluidos")

    @abstractmethod
    def mostrarfechadelregistro(self):
        if self.__fechadenacimiento > 0:

            print(self.nombre, self.apellido, "nacido en", self.__fechadenacimiento)
        else:

            print(self.nombre, self.apellido, "fallecido en", self.__fechadedefuncion)

class nacimiento(Documentos):

    def ingresodenacimiento(self, sexo, ciudad, nombre, apellido, fechadenacimiento):
       
        self.sexo = sexo
        self.ciudad = ciudad
        self.nombre = nombre
        self.apellido = apellido
        self.__fechadenacimiento = fechadenacimiento

class defuncion(Documentos):

    def ingresodedefuncion(self, sexo, ciudad, nombre, apellido, fechadedefuncion):
   
        self.sexo = sexo
        self.ciudad = ciudad
        self.nombre = nombre
        self.apellido = apellido
        self.__fechadedefuncion = fechadedefuncion


persona = nacimiento(111,111,1995)
persona.ingresodenacimiento("a","a","a","a",1996)
persona.mostrarfechadelregistro