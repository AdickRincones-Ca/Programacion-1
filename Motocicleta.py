
class Vehiculo:  # clase mas abstracta
    # este es el constructor de la clase
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self. modelo = modelo
        self.anio = anio
        print("Vehiculo Creado")

    def encender(self):
        print("Estoy listo para llevarte")


class Automovil(Vehiculo):  # herencia simple: Automovil extiende a Vehiculo
    __galonesGasolina = 0
    transmisionManual = True

    def encender(self):  # ejemplo de Polimorfismo - overriding
        print("Listo para llevarte en este", self.modelo)

    def arrancar(self):
        print("raaahh rahh!!")

    def tocarCorneta(self):
        print("beep beep!")

    def echarGasolina(self, vGalones):  # Encapsulamiento - esto es un setter
        if vGalones <= 1:
            print("con un solo galon, no llegas a ninguna parte")
        else:
            self.__galonesGasolina = vGalones

    def cuantaGasolinaHay(self):  # Encapsulamiento - esto es un getter
        print("Ud. tiene:", self.__galonesGasolina, "galones de Gasolina")
        
class motocicleta(Vehiculo):  #1.- herencia de la clase padre
    __galonesGasolina = 0
    __galonesDesperdiciados = 0
    __velocidad = 0
    valorVelocidad=0
    encendido = False
    
    def encender(self):
        print("listo para arrancar su", self.marca, self.modelo)
        self.encendido += 1
        
    def echarGasolina(self, vGalones):
        sumaGalones = vGalones
        if vGalones > 10:
            self.__galonesDesperdiciados = vGalones - 10
            print("Eso es mucha gasolina, se botaron", self.__galonesDesperdiciados, "galones de gasolina")
        else:
            vGalones = 10 - sumaGalones + vGalones
            self.__galonesGasolina = vGalones
            print("Ahora usted tiene", self.__galonesGasolina, "galones de gasolina")
                                          
    def arrancar(self):
        if self.encendido == True:
            self.valorVelocidad = 10 
            print("ruuum rummm")
        else:
            print("encienda la motocicleta primero")
    
    def acelerar(self, aumentoVelocidad):
        if self.encendido == True:
            self.valorVelocidad += aumentoVelocidad
            print("RUUUMMMM")
        else:
            print("encienda la motocicleta primero")

    def frenar(self, frenado):
        if self.encendido == True:
            if self.valorVelocidad > 0:
                self.valorVelocidad -= frenado
                if self.valorVelocidad <= 0:
                    print("ya hemos frenado totalmente")
                else:
                    self.__velocidad = self.valorVelocidad
                    print("su velocidad actual es", self.__velocidad)
            else:
                print("no nos hemos movido")
        else:
            print("encienda la motocicleta primero")
           

# Ejercicio 5pts.
# Instancie otro objeto.
# 1.- Haga herencia de la clase padre
# 2.- Necesito mas especificidad en la administracion del atributo __galonesGasolina
# 3.- Defina un nvo. atributo protegido.  Defina la administracion del acceso a ese atributo.
# 4.- Haga overriding del metodo arrancar.


# instanciando la clase Vehiculo-Automovil
miCarro = motocicleta("Bera", "Socialista", "2013")
miCarro.encender()
miCarro.echarGasolina(65)
miCarro.arrancar()
miCarro.acelerar(50)
miCarro.frenar(90)
