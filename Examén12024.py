
transacciones = []


def agregar_transaccion():
    fecha = input("Ingrese la fecha de la transacción (dd/mm/aaaa): ")
    tipo = input("Ingrese el tipo de transacción (d=cargo, c=abono): ")
    monto = float(input("Ingrese el monto de la transacción: "))
    transacciones.append({"fecha": fecha, "tipo": tipo, "monto": monto})
    print("Transacción agregada exitosamente.")


def consultar_saldo():
    saldo = 0
    for transaccion in transacciones:
        if transaccion["tipo"] == "c":
            saldo += transaccion["monto"]
        else:
            saldo -= transaccion["monto"]
    print("El saldo actual es: ", saldo)


while True:
    print("Menú de opciones:")
    print("a. Agregar un depósito")
    print("b. Agregar un gasto")
    print("c. Consultar saldo")
    print("d. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "a":
        agregar_transaccion()
    elif opcion == "b":
        agregar_transaccion()
    elif opcion == "c":
        consultar_saldo()
    elif opcion == "d":
        break
    else:
        print("Opción inválida. Intente de nuevo.")