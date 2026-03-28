
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#Le han pedido elaborar un programa para calcular el
#promedio y suma total de salarios que paga un empresario
#mensualmente en su microempresa, con el fin de calcular un incremento
#anual.
#Entrada por trabajador (10): salario, antiguedad_años, y edad para
#poder calcular “promedio de edades”.
#Clasificación por grupos:
#- A: 0–2 años.
#- B: >2–8 años.
#- C: >8 años.
#Incremento según promedio salarial del grupo:
#- A: promedio > 2,000,000 → 4%; si no, 7%.
#- B: promedio > 2,400,000 → 5%; si no, 8%.
#- C: promedio > 3,000,000 → 6%; si no, 10%.
#Salidas por grupo:
#- Promedio de salarios.
#- Suma total de salarios.
#- Porcentaje de incremento a aplicar al grupo (no individual).
#- Promedio de edades (si recogemos edad).

# Cantidad de trabajadores
trabajadores = 10

# Grupo A
suma_A = 0
cont_A = 0
edad_A = 0

# Grupo B
suma_B = 0
cont_B = 0
edad_B = 0

# Grupo C
suma_C = 0
cont_C = 0
edad_C = 0

# Recolección de datos
for i in range(1, trabajadores + 1):
    print(f"\nTrabajador {i}")
    
    salario = float(input("Salario: "))
    antiguedad = float(input("Antigüedad (años): "))
    edad = int(input("Edad: "))

    # Clasificación
    if antiguedad <= 2:
        suma_A += salario
        cont_A += 1
        edad_A += edad

    elif antiguedad <= 8:
        suma_B += salario
        cont_B += 1
        edad_B += edad

    else:
        suma_C += salario
        cont_C += 1
        edad_C += edad

# Función para calcular resultados por grupo
def calcular_grupo(suma, cont, suma_edades, limite, inc_mayor, inc_menor):
    if cont > 0:
        promedio = suma / cont
        promedio_edad = suma_edades / cont
        
        if promedio > limite:
            incremento = inc_mayor
        else:
            incremento = inc_menor
    else:
        promedio = 0
        promedio_edad = 0
        incremento = 0

    return promedio, suma, incremento, promedio_edad

# Cálculos
prom_A, total_A, inc_A, edad_prom_A = calcular_grupo(suma_A, cont_A, edad_A, 2000000, 0.04, 0.07)
prom_B, total_B, inc_B, edad_prom_B = calcular_grupo(suma_B, cont_B, edad_B, 2400000, 0.05, 0.08)
prom_C, total_C, inc_C, edad_prom_C = calcular_grupo(suma_C, cont_C, edad_C, 3000000, 0.06, 0.10)

# Resultados
print("\n=== RESULTADOS ===")

print("\nGrupo A")
print(f"Promedio salarios: ${prom_A:.2f}")
print(f"Suma total: ${total_A}")
print(f"Incremento: {inc_A * 100}%")
print(f"Promedio edades: {edad_prom_A:.2f}")

print("\nGrupo B")
print(f"Promedio salarios: ${prom_B:.2f}")
print(f"Suma total: ${total_B}")
print(f"Incremento: {inc_B * 100}%")
print(f"Promedio edades: {edad_prom_B:.2f}")

print("\nGrupo C")
print(f"Promedio salarios: ${prom_C:.2f}")
print(f"Suma total: ${total_C}")
print(f"Incremento: {inc_C * 100}%")
print(f"Promedio edades: {edad_prom_C:.2f}")

#Realizado por Maria Fernanda Tolosa Angel
