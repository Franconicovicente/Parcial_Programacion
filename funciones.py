import random
import os


lista_postulados = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

I_NRO_LISTA = 0
I_VOTOSTEMPRANO = 1
I_VOTOSTARDE = 2
I_VOTOSNOCHE = 3

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

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
    
def calcular_votos_porcentaje (lista:list):
    
    '''
    Calcula votos totales y muestra el porcentaje total de los votos
    '''
    
    votos_totales = acumular_votos(lista_postulados) 
    lista_porcentajes = [0] * len(lista_postulados)  
    
    
    for i in range(len(lista_postulados)):
        listas = lista_postulados[i]
        votos = listas[1] + listas[2] + listas[3]  
        
        if votos_totales != 0:  
            porcentaje = round((votos / votos_totales) * 100, 2)
        else:
            porcentaje = 0
        lista_porcentajes[i] = porcentaje

    return lista_porcentajes
# 2. Mostrar Votos: Muestra en un lindo formato los siguientes datos: Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche,Porcentaje Voto:

def mostrar_votos ():
    '''
    Muestra en un formato mas leible para el usuario los datos adquiridos de la lista 
    del centro de estudiantes
    '''
    porcentajes = calcular_votos_porcentaje(lista_postulados)
    for i in range(len(lista_postulados)):
        resultado = lista_postulados[i]
        porcentaje = porcentajes[i]
        print(f"Nro de lista: {resultado[0]}\nVotos del turno mañana: {resultado[1]}\nVotos del turno tarde: {resultado[2]}\nVotos del turno noche: {resultado[3]}\nPorcentaje: {porcentaje}% de votos.")

# 3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de votos que tuvieron en el turno mañana.

def ordenar_votos_turno_mañana (lista:list):
    '''
    Ordena los votos de mayor a menor de acuerdo a la cantidad de votos basado en el turno mañana. 
    '''
    for i in range(len(lista)-1):
        for j in range(i+1,(len(lista))):
            if lista[i][1] < lista[j][1]:
                voto_aux = lista[i]

                lista[i] = lista[j]
                lista[j] = voto_aux


# 4. No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos los votos
def calcular_porcentaje(lista_postulados:list):
    '''
    Calcula el porcentaje de votos de la lista y muestra a las listas que tengan menos del 5% de los votos
    Dice que lista es, y la acompaña con un texto
    '''
    votos_totales = acumular_votos(lista_postulados) 
    retorno = False
    for i in range(len(lista_postulados)):
        listas = lista_postulados[i]
        votos = listas[1] + listas[2] + listas[3]  
        numero_lista = lista_postulados[i][I_NRO_LISTA]
        
        if votos_totales != 0:  
            porcentaje = round((votos / votos_totales) * 100, 2)
        else:
            porcentaje = 0

        if porcentaje < 5:    
            print(f"La lista {numero_lista} no superó el 5% de los votos")
            retorno = True
    
    if retorno == False:
        print("Ninguna lista tuvo menos del 5% de los votos")
# 5. Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos
# fueron a votar.
def mostrar_turno_que_mas_voto(lista:list):
    '''
    Cuenta la cantidad de alumnos que votan en cada turno, y muestra con un mensaje que turno fue el que más votó
    '''
    acumulador_mañana = 0
    acumulador_tarde = 0
    acumulador_noche = 0

    for i in range(len(lista)):
        acumulador_mañana += lista[i][I_VOTOSTEMPRANO]
        acumulador_tarde += lista[i][I_VOTOSTARDE]
        acumulador_noche += lista[i][I_VOTOSNOCHE]

    if acumulador_mañana > acumulador_tarde and acumulador_mañana > acumulador_noche:
        print(f"En las elecciones, el turno que mas fue a votar fue el turno mañana ({acumulador_mañana} votos)")
    elif acumulador_tarde > acumulador_noche:
        print(f"En las elecciones, el turno que mas fue a votar fue el turno tarde ({acumulador_tarde} votos)")
    else:
        print(f"En las elecciones, el turno que mas fue a votar fue el turno noche ({acumulador_noche} votos)")

# 6. Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única
# forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.

def acumular_votos(lista_postulados:list) -> int:
    '''
    Cuenta los votos totales de los alumnos
    '''
    total_votos = 0
    for listas in lista_postulados:
        for votos in listas[1:]:
            total_votos += votos

    return total_votos

def calcular_porcentaje_por_partido(lista_postulados:list) -> int:
    '''
    Calcula el porcentaje de votos de la lista para saber si
    hay segunda vuelta o no, retorna True o False.
    '''
    votos_totales = acumular_votos(lista_postulados)
    retorno = False

    for listas in lista_postulados:
        votos = 0
        for voto in listas[1:]:
            votos += voto
        
        if votos != 0:
            porcentaje = round((votos/votos_totales) * 100, 2)

        if porcentaje > 50:
            retorno = True

    return retorno

def verificar_segunda_vuelta(lista:list):
    '''
    Verifica cuanto porcentaje de voto tienen los candidatos, si uno supera el 50% 
    no hay ballotage.
    En caso de que ninguno supere el 50% se vota de nuevo (segunda vuelta)
    '''
    estado_vueltas = calcular_porcentaje_por_partido(lista_postulados)
    
    if estado_vueltas == True:
        print("No hay ballotage!")
    else:
        print("Hay ballotage!")


#  7. Realizar segunda vuelta:Se encarga de realizar la segunda vuelta electoral con los
# dos candidatos más votados. Se le pide al usuario la cantidad de alumnos que fueron
# a votar en cada turno en la segunda vuelta y de manera random se calculan los votos
# del primer y segundo candidato en cada turno. Al final de ello se calcula el porcentaje
# final de cada lista y se muestra al ganador de las elecciones.
# NOTA: Solo se accede si hay la opción 6 verificó que hay segunda vuelta, sino indicar
# que no hubo segunda vuelta.
# La cantidad de votos por cada turno debe ser la misma que hubo en la primer vuelta

def calcular_lista_mas_votadas(lista_postulados:list):
    '''
    
    '''
    no_hay_ballotage = calcular_porcentaje_por_partido(lista_postulados)
    lista_primer_lugar = []
    lista_segundo_lugar = []
    votos_primer_lugar = 0
    votos_segundo_lugar = 0

    if no_hay_ballotage == False:
        for listas in lista_postulados:
            numero_lista = listas[0]
            votos = 0
            for voto in listas[1:]:
                votos += voto
            
            if votos > votos_primer_lugar:
                votos_segundo_lugar = votos_primer_lugar
                lista_segundo_lugar = lista_primer_lugar

                votos_primer_lugar = votos
                lista_primer_lugar = numero_lista
            
            elif votos > votos_segundo_lugar:
                votos_segundo_lugar = votos
                lista_segundo_lugar = numero_lista

        print(f"Lista primer lugar: {lista_primer_lugar} con {votos_primer_lugar} votos\nLista segundo lugar: {lista_segundo_lugar} con {votos_segundo_lugar} votos")

        alumnos_que_fueron_a_votar = int(input("Cuantos alumnos fueron a votar a la segunda vuelta?: "))
        votos_1 = random.randint(0, alumnos_que_fueron_a_votar)
        votos_2 = alumnos_que_fueron_a_votar - votos_1

        votos_primer_candidato = round( (votos_1 / alumnos_que_fueron_a_votar) * 100, 2 )
        votos_segundo_candidato = round( (votos_2 / alumnos_que_fueron_a_votar) * 100, 2 )
        if votos_primer_candidato > votos_segundo_candidato:
            print(f"Lista ganadora: {lista_primer_lugar} con el {votos_primer_candidato}% de los votos\nLista que quedó en segundo lugar: {lista_segundo_lugar} con el {votos_segundo_candidato}% de los votos")
        else:
            print(f"Lista ganadora: {lista_segundo_lugar} con el {votos_segundo_candidato}% de los votos\nLista que quedó en segundo lugar: {lista_primer_lugar} con el {votos_primer_candidato}% de los votos")
    else:
        print("No se puede hacer segunda vuelta porque una lista supero el 50% de los votos")