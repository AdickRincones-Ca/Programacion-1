from abc import ABC, abstractmethod



class cuentas(ABC):
    def __init__(self, numerodecuenta):
        self.numerodecuenta = numerodecuenta
        self.capital = 0
        self.intereses = 0 
        self.tiempo = 0 
        self.tasadeinteres = 2
        self.interesesabonados = False
        self.dineroenlacuenta = False
        print("Su cuenta ha sido creada")

    def consularsaldo(self):
        print(f"Su saldo actual es: {self.capital}")

    @abstractmethod
    def depositar(self, ingreso):
        self.capital += ingreso
        if self.capital > 0:
            self.dineroenlacuenta = True

    @abstractmethod
    def retirar(self, retiro):
        if retiro > self.capital:
            print("Saldo insuficiente")
        elif self.dineroenlacuenta == True:
            self.capital -= retiro
        else: 
            print("Usted no tiene dinero en la cuenta") 

    def abonodeintereses(self):
        self.intereses = self.capital*self.tasadeinteres*self.tiempo
        

class ahorro(cuentas):   

    def depositar(self, ingreso):
        super().depositar(ingreso)
    
    def retirar(self, retiro, tiempo):
        self.tiempo = tiempo
        super().abonodeintereses()
        self.capital += self.intereses
        super().retirar(retiro)

class plazofijo(cuentas):  

    def depositar(self, ingreso, tiempo):
        self.tiempo = tiempo
        super().depositar(ingreso)
        super().abonodeintereses()
        self.intereses += self.capital*0.10
        self.capital += self.intereses
    
    def retirar(self, retiro):
        super().retirar(retiro)

Ahorro = plazofijo(111111)
Ahorro.depositar(500, 5)
Ahorro.consularsaldo()
Ahorro.retirar(200)
Ahorro.consularsaldo()