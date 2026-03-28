
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA


# Variables acumuladoras
total_horas = 0
deportivo = 0
cultural = 0
noticias = 0
peliculas = 0
pagan_mas = 0

# Número de personas (muestra fija)
personas = 50

# Ciclo
for i in range(1, personas + 1):
    print(f"\nPersona {i}")

    # Horas de TV
    horas = float(input("Horas de TV por semana: "))
    total_horas += horas

    # Tipo de canal
    print("Tipo de canal preferido:")
    print("1. Deportivo")
    print("2. Cultural")
    print("3. Noticias")
    print("4. Películas")
    
    canal = input("Seleccione una opción (1-4): ")

    if canal == "1":
        deportivo += 1
    elif canal == "2":
        cultural += 1
    elif canal == "3":
        noticias += 1
    elif canal == "4":
        peliculas += 1
    else:
        print("Opción inválida")

    # Pago
    pago = input("¿Pagaría más de $50.000? (si/no): ").lower()
    if pago == "si":
        pagan_mas += 1

    # Edad (solo se pide, no se usa en cálculos)
    edad = int(input("Edad: "))

# Resultados
print("\n=== RESULTADOS DE LA ENCUESTA ===")
print(f"Total de horas semanales: {total_horas}")
print(f"Personas que pagarían más de $50.000: {pagan_mas}")

print("\nPreferencias de canal:")
print(f"Deportivo: {deportivo}")
print(f"Cultural: {cultural}")
print(f"Noticias: {noticias}")
print(f"Películas: {peliculas}")