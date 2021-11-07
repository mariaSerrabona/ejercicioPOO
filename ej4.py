class CuentaBancaria:

    ID=0    #texto
    nombre_titular=0    #texto
    fecha_apertura=0    #texto
    num_cuenta=0    #int
    saldo=0    #int


    def retirar_dinero(self, cantidad_retirar):

        # sacar una cantidad de dinero determinada
        if self.saldo<cantidad_retirar:
            return('No puedas sacar tanto dinero de tu cuenta porque no tienes saldo suficiente')

        else:
            saldo_restante=self.saldo-cantidad_retirar
            saldo_restante=str(saldo_restante)
            return ('cantidad retirada, sus saldo restante es de: '+saldo_restante)


    def ingresar_dinero(self , num_cuenta, cantidad_ingresar):
        #método de ingresar dinero, se pasa una cantidad por parámetro y se ingresa en la cuenta
        saldo_total=self.saldo+cantidad_ingresar
        return('Dinero ingresado. Tiene una cantidad total de: '+str(saldo_total))


    def TransferirDinero(self, num_cuenta1, num_cuenta2, dinero_transferido):
        retirar_dinero( num_cuenta1, dinero_transferido )
        ingresar_dinero(num_cuenta2, dinero_transferido)
        return ('Dinero total transferido: '+str(dinero_transferido))



class CuentaFija(CuentaBancaria):
    #se crea un tipo de cuenta bancaria con todos los atibutos correspondientes
    cantidadRetirar=10
    num_cuenta=0
    if(CuentaBancaria.retirar_dinero(num_cuenta, cantidad_retirar)==True):
        dinero_restante
        dinero_restante=CuentaBancaria.saldo-cantidad_retirar-(cantidad_retirar*0.05)


    CuentaBancaria.retirar_dinero(num_cuenta, cantidad_retirar)

