# Sistema control
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

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