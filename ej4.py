class CuentaBancaria:

    ID=0    #texto
    nombre_titular=0    #texto
    fecha_apertura=0    #texto
    num_cuenta=0    #int
    saldo=0    #int


    def RetirarDinero(num_cuenta, cantidadRetirar):

        # sacar una cantidad de dinero determinada
        if saldo<cantidadRetirar:
            return('No puedas sacar tanto dinero de tu cuenta porque no tienes saldo suficiente')

        else:
            saldoRestante=saldo-cantidadRetirar
            saldoRestante=str(saldoRestante)
            return ('cantidad retirada, sus saldo restante es de: '+saldoRestante)


    def IngresarDinero(num_cuenta, cantidadIngresar):
        #método de ingresar dinero, se pasa una cantidad por parámetro y se ingresa en la cuenta
        saldoTotal=saldo+cantidadIngresar
        return('Dinero ingresado. Tiene una cantidad total de: '+str(saldoTotal))


    def TransferirDinero(num_cuenta1, num_cuenta2, dineroTransferido):
        RetirarDinero(num_cuenta1, dineroTransferido )
        IngresarDinero(num_cuenta2, dineroTransferido)
        return ('Dinero total transferido: '+str(dineroTransferido))



class CuentaFija(CuentaBancaria):
    #se crea un tipo de cuenta bancaria con todos los atibutos correspondientes
    cantidadRetirar=10
    num_cuenta=0
    if(CuentaBancaria.RetirarDinero(num_cuenta, cantidadRetirar)==True):
        dinero_restante
        dinero_restante=CuentaBancaria.saldo-cantidadRetirar-(cantidadRetirar*0.05)


    CuentaBancaria.RetirarDinero(num_cuenta, cantidadRetirar)

