
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


# Cantidad de personas
personas = 10

# Equipos (puedes ajustar nombres)
equipos = ["nacional", "millonarios", "america", "junior"]

# Diccionarios para acumular datos
conteo_equipos = {e: 0 for e in equipos}
edades_equipos = {e: 0 for e in equipos}
dias_equipos = {e: 0 for e in equipos}

# Artículos
articulos = {"camiseta": 0, "chaqueta": 0, "gorra": 0, "morral": 0}

# Recolección de datos
for i in range(1, personas + 1):
    print(f"\nFanático {i}")

    equipo = input("Equipo favorito (nacional/millonarios/america/junior): ").lower()

    if equipo in equipos:
        conteo_equipos[equipo] += 1
    else:
        print("Equipo no válido ❌")
        continue

    articulo = input("Artículo preferido (camiseta/chaqueta/gorra/morral): ").lower()
    if articulo in articulos:
        articulos[articulo] += 1
    else:
        print("Artículo no válido ❌")

    edad = int(input("Edad: "))
    edades_equipos[equipo] += edad

    dias = int(input("Días que asiste al estadio al año: "))
    dias_equipos[equipo] += dias

# Resultados
print("\n=== RESULTADOS ===")

# Cantidad por equipo
print("\nFanáticos por equipo:")
for e in equipos:
    print(f"{e.capitalize()}: {conteo_equipos[e]}")

# Promedio de edades por equipo
print("\nPromedio de edades por equipo:")
for e in equipos:
    if conteo_equipos[e] > 0:
        promedio = edades_equipos[e] / conteo_equipos[e]
    else:
        promedio = 0
    print(f"{e.capitalize()}: {promedio:.2f}")

# Promedio de días por equipo
print("\nPromedio de asistencia al estadio por equipo:")
for e in equipos:
    if conteo_equipos[e] > 0:
        promedio = dias_equipos[e] / conteo_equipos[e]
    else:
        promedio = 0
    print(f"{e.capitalize()}: {promedio:.2f}")

# Artículo más preferido
articulo_preferido = max(articulos, key=articulos.get)

print(f"\nArtículo más preferido: {articulo_preferido}")

#Realizado por Maria Fernanda Tolosa Angel
