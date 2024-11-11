from funciones import *


while True:
    print("Menu UTN FRA\n")
    print("Elija una opcion...\n1.Cargar votos.\n2.Mostrar votos.\n3.Ordenar votos turno mañana.\n4.No te votó nadie...\n5.Turno que mas fue a votar.\n6.Hay ballotage?.\n7.Hacer segunda vuelta.\n8.Salir.")
    opcion = int(input("Su opcion: "))

    if opcion == 1:
        print("Carga de datos...")
        cargar_votos(lista_postulados)

    elif opcion == 2:
        print("Mostrando votos...")
        mostrar_votos()

    elif opcion == 3:
        print("Mostrando votos segun el turno mañana...")
        ordenar_votos_turno_mañana(lista_postulados)
        mostrar_votos()

    elif opcion == 4: 
        calcular_porcentaje(lista_postulados)

    elif opcion == 5:
        mostrar_turno_que_mas_voto(lista_postulados)

    elif opcion == 6:
        print("Verificando si hay segunda vuelta...")
        verificar_segunda_vuelta(lista_postulados)

    elif opcion == 7:
        calcular_lista_mas_votadas(lista_postulados)

    elif opcion == 8:
        break
    
    else:
        print("Ingrese una opción correcta...")

    limpiar_consola()
