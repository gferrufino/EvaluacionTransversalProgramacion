import random
import os
import statistics
import csv

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez",
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

#asignador de sueltos aleatorios

def asignar_sueldos():
    sueldos = {trabajador: random.randint(
        300000, 2500000) for trabajador in trabajadores}
    return sueldos

#clasificacion de sueldo

def clasificar_sueldos(sueldos):
    menores = {k: v for k, v in sueldos.items() if v < 800000}
    medios = {k: v for k, v in sueldos.items() if 800000 <= v <= 2000000}
    mayores = {k: v for k, v in sueldos.items() if v > 2000000}

    print("Sueldos menores a $800.000")
    for trabajador, sueldo in menores.items():
        print(f"{trabajador}: ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    for trabajador, sueldo in medios.items():
        print(f"{trabajador}: ${sueldo}")

    print("\nSueldos mayores a $2.000.000")
    for trabajador, sueldo in mayores.items():
        print(f"{trabajador}: ${sueldo}")

#estadisticas de los sueldos

def ver_estatistica(sueldos):
    sueldos_list = list(sueldos.values())
    max_sueldo = max(sueldos_list)
    min_sueldo = min(sueldos_list)
    promedio_sueldo = statistics.mean(sueldos_list)
    media_geometrica = statistics.geometric_mean(sueldos_list)

    print(f"Sueldo mas alto: ${max_sueldo}")
    print(f"Sueldo mas bajo: ${min_sueldo}")
    print(f"Promedio de sueldos: ${promedio_sueldo}")
    print(f"Media geometrica de los sueldos: ${media_geometrica}")

#reporte de sueldos lo intente pero no se si habra salido bien me arrojaba como muchos decimales
#cuando lo abri en excel como que los montos no me calzaban pero no supe como arreglarlo

def reporte_sueldos(sueldos):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path =os.path.join(current_directory, 'reporte_sueldos.csv')
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre trabajador", "Sueldo total",
                        "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for trabajador, sueldo in sueldos.items():
            afp = sueldo * 0.12
            fonasa = sueldo * 0.07
            sueldosindescuento = sueldo - fonasa - afp
            writer.writerow(
                [trabajador, sueldo, fonasa, afp, sueldosindescuento])

    print(f"se han generado los sueldos exitosamente en: '{file_path}'")

#definicion y print del menu
    
def menu():
    sueldos = asignar_sueldos()
    while True:
        print("menu:")
        print("1. Asignar sueldos aleatorios.")
        print("2. Clasificar sueldos.")
        print("3. veer estadisticas.")
        print("4. Reporte de sueldos.")
        print("5. Salir del programa.")

#las opciones del menu
        
        opcion = input("Selecciona la opcion que prefieras: ")

        if opcion == '1':
            sueldos = asignar_sueldos()
            print("los sueldos han sido asignados con exito :D.")
        elif opcion == '2':
            clasificar_sueldos(sueldos)
        elif opcion == '3':
            ver_estatistica(sueldos)
        elif opcion == '4':
            reporte_sueldos(sueldos)
        elif opcion == '5':
            print("Finalizando el programa")
            print("Desarrollado por gabriel ferrufino rivera")
            print("RUT 19.764.835-k")
            break
        else:
            print("la opcion que elegiste no es valida porfavor intenta nuevamente")


if __name__ == "__main__":
    menu()

#crei que la prueba seria con funciones aparte pero en la prueba lo busque y
#no estaba, no se no lei bien o de imbecil o solo no estaba
