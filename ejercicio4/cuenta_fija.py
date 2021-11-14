import cuenta_bancaria

class CuentaFija(cuenta_bancaria.CuentaBancaria):

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
        saldo_restante=self.get_saldo()-(cantidad+dinero_retenido)
        self.set_saldo()==saldo_restante
        print('se ha retirado un total de: '+ cantidad+ 'saldo restante en la cuenta: '+  saldo_restante)

    else:
        def retirar_dinero(self, cantidad_retirar):
            return super().retirar_dinero(cantidad_retirar)