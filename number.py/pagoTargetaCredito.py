# Reciba por consola el valor de una compra
# Que puedan ingresar el numero de cuotas
# Valor de la cuota
# Usando while queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago.


compra = float(input("ingrese el valor de la compra"))
cuotas = int(input("ingrese el numero de cuotas"))
valor = compra / cuotas
print("total de la cuota es",valor)
cuotaActual = 1
saldoPendiente = compra
while  cuotaActual <= cuotas:
    print("Cuota ",cuotaActual," valor de cuota ",valor,"Saldo restante",saldoPendiente)
    cuotaActual+=1
    saldoPendiente-=valor
        
        