import random


lista_postulados = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

I_NRO_LISTA = 0
I_VOTOSTEMPRANO = 1
I_VOTOSTARDE = 2
I_VOTOSNOCHE = 3


# 1. Cargar Votos: Se realiza una carga secuencial de todos los votos de cada una de las
# cinco listas.

def cargar_votos (lista:list):
    '''
    Permite cargar los datos de cada lista que hay.
    Devuelve la lista con los datos ya cargados
    '''
    
    for fil in range(len(lista)):
        numero_lista = int(input("Ingrese el nro de lista: "))
        while numero_lista < 99 or numero_lista > 999:
            numero_lista = int(input("Error, reingrese nro de lista: "))
        
        votos_mañana = int(input("Ingrese la cantidad de votos del turno mañana: "))
        while votos_mañana < 0:
            votos_mañana = int(input("Error, ingrese una cantidad de votos valida: "))
        
        votos_tarde = int(input("Ingrese la cantidad de votos del turno tarde: "))
        while votos_tarde < 0:
            votos_tarde = int(input("Error, ingrese una cantidad de votos valida: "))
    
        votos_noche = int(input("Ingrese la cantidad de votos del turno noche: "))
        while votos_noche < 0:
            votos_noche = int(input("Error, ingrese una cantidad de votos valida: "))

        lista[fil][I_NRO_LISTA] = numero_lista
        lista[fil][I_VOTOSTEMPRANO] = votos_mañana
        lista[fil][I_VOTOSTARDE] = votos_tarde
        lista[fil][I_VOTOSNOCHE] = votos_noche


    return lista


# 2. Mostrar Votos: Muestra en un lindo formato los siguientes datos: Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche,Porcentaje Voto:
# 4. No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos los votos

def mostrar_votos (lista:list):
    '''
    Muestra en un formato mas leible para el usuario los datos adquiridos de la lista 
    del centro de estudiantes
    Tambien calcula el porcentaje de votos de la lista y en caso de tener menos del 5% de los votos
    Dice que lista es, y la acompaña con un texto
    '''
    resultado = cargar_votos(lista_postulados)

    print("Datos de la lista...")
    print("")
    for resultado in lista_postulados:
        print(f"Nro de lista: {resultado[0]}")
        print(f"Votos del turno mañana: {resultado[1]}")
        print(f"Votos del turno tarde: {resultado[2]}")
        print(f"Votos del turno noche: {resultado[3]}")
        print("=" * 40)

    total_votos = 0

    for listas in lista:
        for votos in listas[1:]:
            total_votos += votos
    
    for listas in lista:
        numero_lista = listas[0]
        votos = 0

        for voto in listas[1:]:
            votos += voto
        
        if votos == 0:
            print(f"Lista nro {numero_lista}: 0% de votos")
        else:
            porcentaje = round((votos / total_votos) * 100, 2)
            print(f"Lista nro {numero_lista}: {porcentaje}% de votos")

            if porcentaje < 5:
                print(f"A la lista {numero_lista} no la votó nadie!")


mostrar_votos(lista_postulados)

# 3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de
# votos que tuvieron en el turno mañana.

def ordenar_votos_turno_mañana (lista:list):
    '''
    Ordena los votos de mayor a menor de acuerdo a la cantidad de votos 
    basado en el turno mañana. Retorna la nueva lista ordenada
    '''

    for i in range(len(lista)-1):
        for j in range(i+1,(len(lista))):
            if lista[i][1] < lista[j][1]:
                voto_aux = lista[i]

                lista[i] = lista[j]
                lista[j] = voto_aux

    return lista

def mostrar_votos_turno_mañana (lista:list):
    '''
    Muestra en un formato mas leible para el usuario los datos adquiridos de la lista 
    del centro de estudiantes
    '''
    
    resultado = ordenar_votos_turno_mañana(lista_postulados)

    print("Datos ordenados de mayor a menor de acuerdo a votos del turno mañana...")
    print("")
    for resultado in lista_postulados:
        print(f"Nro de lista: {resultado[0]}")
        print(f"Votos del turno mañana: {resultado[1]}")
        print(f"Votos del turno tarde: {resultado[2]}")
        print(f"Votos del turno noche: {resultado[3]}")
        print("=" * 40)

mostrar_votos_turno_mañana(lista_postulados)

# 5. Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos
# fueron a votar.

def mostrar_turno_que_mas_voto(lista:list):
    '''
    Cuenta la cantidad de alumnos que votan en cada turno, y muestra con un mensaje 
    el resultado
    '''
    for i in range(len(lista)):
        print(f"En la lista numero {i+1}...")
        if lista[i][I_VOTOSTEMPRANO] > lista[i][I_VOTOSTARDE] and lista[i][I_VOTOSTEMPRANO] > lista[i][I_VOTOSNOCHE]:
            print("Los alumnos que mas fueron a votar fueron los del turno mañana...")
        elif lista[i][I_VOTOSTARDE] > lista[i][I_VOTOSNOCHE]:
            print("Los alumnos que mas fueron a votar fueron los del turno tarde...")
        else:
            print("Los alumnos que mas fueron a votar fueron los del turno noche...")
            

mostrar_turno_que_mas_voto(lista_postulados)

# 6. Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única
# forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.

def verificar_segunda_vuelta(lista:list):
    '''
    Verifica cuanto porcentaje de voto tienen los candidatos, si uno supera el 50% 
    no hay ballotage.
    En caso de que ninguno supere el 50% se vota de nuevo (segunda vuelta)
    '''
    total_votos = 0

    for listas in lista:
        for votos in listas[1:]:
            total_votos += votos
    
    for listas in lista:
        numero_lista = listas[0]
        votos = 0

        for voto in listas[1:]:
            votos += voto
        
        if votos == 0:
            print(f"Lista nro {numero_lista}: 0% de votos")
        else:
            porcentaje = round((votos / total_votos) * 100, 2)
            print(f"Lista nro {numero_lista}: {porcentaje}% de votos")

            if porcentaje > 50:
                print(f"No hay ballotage!")
        
            else: #7. Realizar segunda vuelta
                print(f"Es necesaria una segunda vuelta...")
                print("")


verificar_segunda_vuelta(lista_postulados)

