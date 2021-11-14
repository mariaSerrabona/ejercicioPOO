# pylint: disable=too-many-arguments

from datetime import date
import random
class CuentaBancaria:

    ID=0    #texto
    nombre_titular=''   #texto
    fecha_apertura=date.today()   #texto
    num_cuenta=0    #int
    saldo=0    #int

    #definimso el costructor de la clase cuenta bancaria
    def __init__(self, ID, nombre_titular,fecha_apertura, num_cuenta, saldo ):
        self._ID=ID
        self._nombre_titular=nombre_titular
        self._fecha_apertura=fecha_apertura
        self._num_cuenta=num_cuenta
        self._saldo=saldo

    #creamos todos los getter y setter
    def getID(self):
        return self._ID
    def setID(self, ID):
        self._ID=ID

    def get_nombre_titular(self):
        return self._nombre_titular
    def set_nombre_titular(self, nombre_titular):
        self._nombre_titular=nombre_titular

    def get_fecha_apertura(self):
        return self._fecha_apertura
    def set_fecha_apertura(self, fecha_apertura):
        self._fecha_apertura=fecha_apertura

    def get_num_cuenta(self):
        return self._num_cuenta
    def set_num_cuenta(self, num_cuenta):
        self._num_cuenta=num_cuenta

    def get_saldo(self):
        return self._saldo
    def set_saldo(self, saldo):
        self._saldo=saldo


    #a medida que retiramos el dinero, lo vamos actualizando en a cuenta
    def retirar_dinero(self, cantidad_retirar):
        cantidad_retirar=int(cantidad_retirar)
        # sacar una cantidad de dinero determinada
        if cantidad_retirar>self.get_saldo():
            return('No puedas sacar tanto dinero de tu cuenta porque no tienes saldo suficiente')

        else:
            saldo_restante=self.get_saldo()-cantidad_retirar
            self.set_saldo()=saldo_restante
            saldo_restante=str(saldo_restante)
            return ('cantidad retirada, sus saldo restante es de: '+saldo_restante)

    #a medida que ingresamos dinero, se lo vamos añadiente a la cuenta definida antes
    def ingresar_dinero(self , cantidad_ingresar):
        #método de ingresar dinero, se pasa una cantidad por parámetro y se ingresa en la cuenta
        saldo_total=self.get_saldo()+cantidad_ingresar
        self.set_saldo()==saldo_total
        return('Dinero ingresado. Tiene una cantidad total de: '+str(saldo_total))

    def CrearCuentas():#ID, nombre_titular,fecha_apertura, num_cuenta, sald
        #rellenar los datos con el input de la cuentas bancarias
        #ahcer esto con todos los atributos
        ID=input('Introduzca el id')
        try:
            ID=int(ID)
        except ValueError:
            print('Error de valor, se necesita poner un número entero')
        nombre_titular=input('Introduzca el nombre del titular')
        fecha_apertura=input('Introduzca la fecha de apertura')
        num_cuenta=input('Introduzca el número de cuenta')
        try:
            num_cuenta=int(num_cuenta)
        except ValueError:
            print('Error de valor, se necesita poner un número entero')
        saldo=input('Introduzca el saldo actual de la cuenta')

    def transferir_dinero(self, cantidad_transferida, cuenta):
        if int (cantidad_transferida)>self.get_saldo():
            return (' no se dispone de tanrto dinero en la cuenta como para poder trasnferirlo a otra cuenta')
        else:
            self.retirar_dinero(cantidad_transferida)
            cuenta.ingresar_dinero( cantidad_transferida)

        return ('Dinero total transferido: '+str(cantidad_transferida))

