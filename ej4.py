# pylint: disable=too-many-arguments
class CuentaBancaria:

    ID=0    #texto
    nombre_titular=0    #texto
    fecha_apertura=0    #texto
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


    #a medida que retiramos el dinero, lo vamoa actualizando en a cuenta
    def retirar_dinero(self, cantidad_retirar):
        cantidad_retirar=int(cantidad_retirar)
        # sacar una cantidad de dinero determinada
        if cantidad_retirar>CuentaBancaria.get_saldo:
            return('No puedas sacar tanto dinero de tu cuenta porque no tienes saldo suficiente')

        else:
            saldo_restante=CuentaBancaria.get_saldo-cantidad_retirar
            saldo_restante=str(saldo_restante)
            CuentaBancaria.set_saldo=saldo_restante
            return ('cantidad retirada, sus saldo restante es de: '+saldo_restante)

    #a medida que ingresamos dinero, se lo vamos añadiente a la cuenta definida antes
    def ingresar_dinero(self , cantidad_ingresar):
        #método de ingresar dinero, se pasa una cantidad por parámetro y se ingresa en la cuenta
        saldo_total=CuentaBancaria.get_saldo()+cantidad_ingresar
        CuentaBancaria.set_saldo=saldo_total
        return('Dinero ingresado. Tiene una cantidad total de: '+str(saldo_total))


    def transferir_dinero(self, cantidad_transferida, cuenta):
        if int (cantidad_transferida)>CuentaBancaria.get_saldo:
            return (' no se dispone de tanrto dinero en la cuenta como para poder trasnferirlo a otra cuenta')
        else:
            CuentaBancaria.retirar_dinero(cantidad_transferida)
            cuenta.ingresar_dinero( cantidad_transferida)

        return ('Dinero total transferido: '+str(cantidad_transferida))



class CuentaFija(CuentaBancaria):
    #se crea un tipo de cuenta bancaria con todos los atibutos correspondientes
    cantidadRetirar=10
    num_cuenta=0
    if(CuentaBancaria.retirar_dinero(num_cuenta, cantidad_retirar)==True):
        dinero_restante
        dinero_restante=CuentaBancaria.saldo-cantidad_retirar-(cantidad_retirar*0.05)


    CuentaBancaria.retirar_dinero(num_cuenta, cantidad_retirar)

