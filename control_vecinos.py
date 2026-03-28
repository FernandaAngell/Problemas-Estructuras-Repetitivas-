
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#En un conjunto residencial, cada vecino debe pagar una
#cuota mensual para el mantenimiento. El administrador quiere un
#programa que revise uno por uno a todos los vecinos para lo cual el
#usuario debe ingresar la cantidad de residentes de la unidad residencial
#y el valor de la cuota mensual.
#Por cada vecino, el sistema debe pedir si ya pagó su cuota o no.
#Si el vecino pagó, se registra como “al día”; si no pagó, el programa lo
#registra como “moroso”.
#Este proceso debe repetirse hasta haber revisado a todos los vecinos.
#Al finalizar, el programa muestra cuántas personas están al día y
#cuántas están atrasadas y cuanto es el valor total adeudado por los
#vecinos morosos.


# Solicitar datos iniciales
total_vecinos = int(input("Ingrese la cantidad de residentes: "))
cuota = float(input("Ingrese el valor de la cuota mensual: "))

# Contadores
al_dia = 0
morosos = 0
total_deuda = 0

# Recorrer cada vecino
for i in range(1, total_vecinos + 1):
    print(f"\nVecino {i}")
    pago = input("¿Pagó la cuota? (si/no): ").lower()

    if pago == "si":
        al_dia += 1
    else:
        morosos += 1
        total_deuda += cuota

# Resultados
print("\n=== REPORTE FINAL ===")
print(f"Vecinos al día: {al_dia}")
print(f"Vecinos morosos: {morosos}")
print(f"Total adeudado: ${total_deuda}")

#Realizado por Maria Fernanda Tolosa Angel
