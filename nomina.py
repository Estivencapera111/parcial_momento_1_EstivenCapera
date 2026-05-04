# nomina.py

empleados = []

def registrar_empleado():
    print("\n--- Registrar Empleado ---")
    nombre = input("Nombre del empleado: ")

    while True:
        try:
            salario_base = float(input("Salario base: "))
            dias_trabajados = int(input("Dias trabajados: "))
            break
        except ValueError:
            print("Ingresa valores validos.")

    empleado = {
        "nombre": nombre,
        "salario_base": salario_base,
        "dias_trabajados": dias_trabajados
    }
    empleados.append(empleado)
    print(f"Empleado '{nombre}' registrado correctamente.")

def menu():
    print("\n============================")
    print("  SISTEMA DE NOMINA - StartUp")
    print("============================")
    print("1. Registrar empleado")
    print("2. Calcular nomina")
    print("3. Salir")

def main():
    while True:
        menu()
        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            print("(Modulo en desarrollo...)")
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()