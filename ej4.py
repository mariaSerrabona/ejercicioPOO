# pylint: disable=too-many-arguments

from datetime import date
class CuentaBancaria:

    ID=0    #texto
    nombre_titular=0    #texto
    fecha_apertura=date.datetime   #texto
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
            saldo_restante=str(saldo_restante)
            CuentaBancaria.set_saldo()=saldo_restante
            return ('cantidad retirada, sus saldo restante es de: '+saldo_restante)

    #a medida que ingresamos dinero, se lo vamos añadiente a la cuenta definida antes
    def ingresar_dinero(self , cantidad_ingresar):
        #método de ingresar dinero, se pasa una cantidad por parámetro y se ingresa en la cuenta
        saldo_total=CuentaBancaria.get_saldo()+cantidad_ingresar
        CuentaBancaria.set_saldo()=saldo_total
        return('Dinero ingresado. Tiene una cantidad total de: '+str(saldo_total))


    def transferir_dinero(self, cantidad_transferida, cuenta):
        if int (cantidad_transferida)>CuentaBancaria.get_saldo():
            return (' no se dispone de tanrto dinero en la cuenta como para poder trasnferirlo a otra cuenta')
        else:
            CuentaBancaria.retirar_dinero(cantidad_transferida)
            cuenta.ingresar_dinero( cantidad_transferida)

        return ('Dinero total transferido: '+str(cantidad_transferida))



class CuentaFija(CuentaBancaria):
    #se crea un tipo de cuenta bancaria con todos los atibutos correspondientes
    fecha_vencimiento=date
    cantidad=0
    #comparamos las fechas y si se cumple la condición, entonces cargaremos el 0.05 de la canttidad de penalizacion
    if(fecha_vencimiento>date):
        #habría que hacer lo mimso con las transferencias pero no se cómo ponerlo para que
        #no me lo haga dos veces

        #no se cómo poner al condición de que solo lo haga cuando saque dinero o haga una trasferencia
        CuentaBancaria.retirar_dinero(cantidad)
        dinero_retenido=cantidad*0.05
        saldo_restante=CuentaBancaria.get_saldo()-(cantidad+dinero_retenido)
        CuentaBancaria.set_saldo()=saldo_restante

    else:
        CuentaBancaria.retirar_dinero(cantidad)
        saldo_restante=CuentaBancaria.get_saldo()-cantidad
        CuentaBancaria.set_saldo()=saldo_restante

class CuentaVip(CuentaBancaria):
    #herega todos los atributos de la clase CuentaBancaria pero se le añade un nuevo atributo
    saldo_negativo_max=0
    def retirar_dinero_vip(self, cantidad_retirar):
        if cantidad_retirar> (CuentaVip.get_saldo()+saldo_negativo_max):
            print('se ha excedido el límite de dinero para sacar')
        else:
            CuentaBancaria.set_saldo()=CuentaBancaria.get_saldo()-cantidad_retirar


    def transferir_dinero_vip(self, cantidad_transferida, cuenta):
        if int (cantidad_transferida)>(CuentaBancaria.get_saldo()+saldo_negativo_max):
            print (' no se dispone de tanrto dinero en la cuenta como para poder trasnferirlo a otra cuenta')

        else:
            CuentaBancaria.retirar_dinero(cantidad_transferida)
            cuenta.ingresar_dinero( cantidad_transferida)




