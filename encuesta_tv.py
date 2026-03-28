
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#Un nuevo operador de televisión por cable desea ofrecer
#nuevos servicios en su ciudad. Para esto, se requiere saber en una
#muestra de 50 personas:
#- Cuántas horas a la semana invierten en ver televisión.
#- Qué tipo de canal prefieren ver: deportivo, cultural, de noticias o
#de películas.
#- Cuántas personas están dispuestas a pagar más de 50 mil pesos
#por el servicio de televisión.
#- La edad de la persona
#El programa debe mostrar:
#- El promedio de horas semanales que invierten los encuestados en
#ver televisión.
#- La cantidad de personas interesadas en cada canal: deportivo,
#cultural, de noticias o de películas.
#- La cantidad de personas que están dispuestas a pagar más de 50
#mil pesos por el servicio.
#- El promedio de edades de los encuestados.

# Variables acumuladoras
total_horas = 0
total_edades = 0
deportivo = 0
cultural = 0
noticias = 0
peliculas = 0
pagan_mas = 0

# Número de personas
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
        print("Opción inválida ❌")

    # Pago
    pago = input("¿Pagaría más de $50.000? (si/no): ").lower()
    if pago == "si":
        pagan_mas += 1

    # Edad
    edad = int(input("Edad: "))
    total_edades += edad

# Cálculos finales
promedio_horas = total_horas / personas
promedio_edades = total_edades / personas

# Resultados
print("\n=== RESULTADOS DE LA ENCUESTA ===")
print(f"Promedio de horas semanales: {promedio_horas:.2f}")
print(f"Promedio de edades: {promedio_edades:.2f}")

print("\nPersonas por tipo de canal:")
print(f"Deportivo: {deportivo}")
print(f"Cultural: {cultural}")
print(f"Noticias: {noticias}")
print(f"Películas: {peliculas}")

print(f"\nPersonas que pagarían más de $50.000: {pagan_mas}")

#Realizado por Maria Fernanda Tolosa Angel
