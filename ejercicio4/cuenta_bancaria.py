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
        if cantidad_retirar>CuentaBancaria.get_saldo():
            return('No puedas sacar tanto dinero de tu cuenta porque no tienes saldo suficiente')

        else:
            saldo_restante=CuentaBancaria.get_saldo()-cantidad_retirar
            CuentaBancaria.set_saldo()==saldo_restante
            saldo_restante=str(saldo_restante)
            return ('cantidad retirada, sus saldo restante es de: '+saldo_restante)

    #a medida que ingresamos dinero, se lo vamos añadiente a la cuenta definida antes
    def ingresar_dinero(self , cantidad_ingresar):
        #método de ingresar dinero, se pasa una cantidad por parámetro y se ingresa en la cuenta
        saldo_total=CuentaBancaria.get_saldo()+cantidad_ingresar
        CuentaBancaria.set_saldo()==saldo_total
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
        if int (cantidad_transferida)>CuentaBancaria.get_saldo():
            return (' no se dispone de tanrto dinero en la cuenta como para poder trasnferirlo a otra cuenta')
        else:
            CuentaBancaria.retirar_dinero(cantidad_transferida)
            cuenta.ingresar_dinero( cantidad_transferida)

        return ('Dinero total transferido: '+str(cantidad_transferida))



class CuentaFija(CuentaBancaria):

    #generamos una fecha aleatoria que será la fecha de vencimiento
    def fecha_vencimiento():
        dia=str(random.randint(0,30))
        mes=str(random.randint(0,12))
        año=str(random.randint(2021,2030))
        return (dia+'/'+mes+'/'+año)
    #se crea un tipo de cuenta bancaria con todos los atibutos correspondientes
    fecha_vencimiento=fecha_vencimiento()
    cantidad=0
    #comparamos las fechas y si se cumple la condición, entonces cargaremos el 0.05 de la canttidad de penalizacion

    def retirar_dinero(self, cantidad_retirar):
        return super().retirar_dinero(cantidad_retirar)
    if(fecha_vencimiento>str(date.today)):
        dinero_retenido=cantidad*0.05
        print('Se han cobrado intereses de un total de: '+dinero_retenido)
        saldo_restante=CuentaBancaria.get_saldo()-(cantidad+dinero_retenido)
        CuentaBancaria.set_saldo()==saldo_restante
        print('se ha retirado un total de: '+ cantidad+ 'saldo restante en la cuenta: '+  saldo_restante)

    else:
        def retirar_dinero(self, cantidad_retirar):
            return super().retirar_dinero(cantidad_retirar)

class CuentaVip(CuentaBancaria):
    #herega todos los atributos de la clase CuentaBancaria pero se le añade un nuevo atributo
    saldo_negativo_max=0
    def retirar_dinero_vip(self, cantidad_retirar):
        if cantidad_retirar> (CuentaVip.get_saldo()+saldo_negativo_max):
            print('se ha excedido el límite de dinero para sacar')
        else:
            CuentaBancaria.set_saldo()==CuentaBancaria.get_saldo()-cantidad_retirar


    def transferir_dinero_vip(self, cantidad_transferida, cuenta):
        if int (cantidad_transferida)>(CuentaBancaria.get_saldo()+saldo_negativo_max):
            print (' no se dispone de tanrto dinero en la cuenta como para poder trasnferirlo a otra cuenta')

        else:
            CuentaBancaria.retirar_dinero(cantidad_transferida)
            cuenta.ingresar_dinero( cantidad_transferida)




