from main1

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez",
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

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