#Nombre: Maria Fernanda Tolosa Angel
#Grupo: 277
#Porgrama: Fundamentos de programación
#Código Fuente: Autoría propia

#En un proceso industrial, un horno debe mantener su
#temperatura dentro de un rango operativo entre 180 grados Celsius y
#200 grados Celsius. El sistema debe monitorear continuamente la
#temperatura y emitir una alerta si se sale del rango.
#El sistema debe monitorear continuamente la temperatura del horno. En
#cada iteración:
#Solicite una temperatura entera positiva en °C (valide).
#Si temperatura > 200 → “Alerta: enfriamiento”.
#Si temperatura < 180 → “Alerta: calentamiento”.
#En caso contrario → “Temperatura óptima”.
#Pregunte “¿Desea continuar? (1: sí, 0: no)”. Si el usuario ingresa 0,
#termina el monitoreo.


def solicitar_temperatura():
    while True:
        try:
            temp = int(input("Ingrese la temperatura del horno (°C): "))
            if temp > 0:
                return temp
            else:
                print("⚠️ Error: la temperatura debe ser un número entero positivo.")
        except ValueError:
            print("⚠️ Error: debe ingresar un número entero válido.")


def evaluar_temperatura(temp):
    if temp > 200:
        return "Alerta: enfriamiento"
    elif temp < 180:
        return "Alerta: calentamiento"
    else:
        return "Temperatura óptima"


def desea_continuar():
    while True:
        opcion = input("¿Desea continuar? (1: sí, 0: no): ")
        if opcion in ["1", "0"]:
            return opcion == "1"
        else:
            print("⚠️ Opción inválida. Ingrese 1 o 0.")


def main():
    print("=== SISTEMA DE MONITOREO DE TEMPERATURA ===")

    continuar = True
    while continuar:
        temperatura = solicitar_temperatura()
        resultado = evaluar_temperatura(temperatura)

        print(f"Resultado: {resultado}")

        continuar = desea_continuar()

    print("🔚 Monitoreo finalizado.")


# Ejecutar programa
if __name__ == "__main__":
    main()


#Realizado por Maria Fernanda Tolosa Angel
