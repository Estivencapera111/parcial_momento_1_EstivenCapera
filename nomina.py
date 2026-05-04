# nomina.py

empleados = []

SALARIO_MINIMO = 1300000
AUXILIO_TRANSPORTE = 160000
DESCUENTO_SALUD_PENSION = 0.08

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

def calcular_nomina():
    if not empleados:
        print("\nNo hay empleados registrados.")
        return

    print("\n--- Calculo de Nomina ---")

    for emp in empleados:
        nombre = emp["nombre"]
        salario_base = emp["salario_base"]
        dias_trabajados = emp["dias_trabajados"]

        salario_proporcional = (salario_base / 30) * dias_trabajados

        auxilio = 0
        if salario_base < (2 * SALARIO_MINIMO):
            auxilio = AUXILIO_TRANSPORTE

        descuento = salario_proporcional * DESCUENTO_SALUD_PENSION

        salario_neto = salario_proporcional + auxilio - descuento

        print(f"\nEmpleado: {nombre}")
        print(f"  Salario proporcional ({dias_trabajados} dias): ${salario_proporcional:,.0f}")
        print(f"  Auxilio de transporte:              ${auxilio:,.0f}")
        print(f"  Descuento salud + pension (8%):    -${descuento:,.0f}")
        print(f"  SALARIO NETO A PAGAR:               ${salario_neto:,.0f}")
        print("  " + "-"*40)

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
            calcular_nomina()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()