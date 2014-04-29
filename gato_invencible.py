#Biblioteca para funciones especificas del sistema
import sys

# Valores : Ganador computadora :1
#           Ganador persona: -1
#           Empate 0

MAX = 1
MIN = -1
global jugada_computadora
 
def minimax(tablero, jugador):
    global jugada_computadora
    # Existe ganador o empate?
    if juego_terminado(tablero):
        return [ganador(tablero), 0]
    # Generar posibles jugadas
    movimientos=[]
    for jugada in range(0,len(tablero)):
        if tablero[jugada] == 0:
            tableroaux=tablero[:]
            tableroaux[jugada] = jugador
 
            puntuacion = minimax(tableroaux, jugador*(-1))
            movimientos.append([puntuacion, jugada])
  
    if jugador == MAX:
        movimiento = max(movimientos)
        jugada_computadora = movimiento[1]
        return movimiento
    else:
        movimiento = min(movimientos)
        return movimiento[0]
 
 
def juego_terminado(tablero):
    # empate?
    no_empate = False
    for i in range(0,len(tablero)):
        if tablero[i] == 0:
            no_empate = True
    # ganador?
    if ganador(tablero) == 0 and no_empate:
        return False
    else:
        return True
 
def ganador(tablero):
    lineas = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    ganador = 0
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] and tablero[linea[0]] == tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador = tablero[linea[0]]
    return ganador
 
def dibujar_tablero(tablero):
    for i in range(0,3):
        for j in range(0,3):
            if tablero[i*3+j] == MAX:
                print 'X',
            elif tablero[i*3+j] == MIN:
                print 'O',
            else:
                print '.',
        print ''
 
def juega_humano(tablero):
    tira_humano=False
    while not tira_humano:
        casilla = input ("Introduce una de las casillas: ")
        if str(casilla) in '0123456789' and len(str(casilla)) == 1 and tablero[casilla-1] == 0:
            if casilla == 0:
                sys.exit(0)
            tablero[casilla-1]=MIN
            tira_humano=True
    return tablero
 
def juega_computadora(tablero):
    global jugada_computadora
    puntuacion = minimax(tablero[:], MAX)
    tablero[jugada_computadora] = MAX
    return tablero
 
def inicia_juego():
    print 'Introduce una de las casillas "1,2,3,4,5,6,7,8,9" o 0 para salir'
    tablero = [0,0,0,0,0,0,0,0,0]
 
    while (True):
        dibujar_tablero(tablero)
        tablero = juega_humano(tablero)
        if juego_terminado(tablero):
            break
        tablero = juega_computadora(tablero)
        if juego_terminado(tablero):
            break
 
    dibujar_tablero(tablero)
    resultado = ganador(tablero)
    if resultado == 0:
        gana = 'Empate :) '
    elif resultado == MIN:
        gana = 'Gana Jugador'
    else:
        gana = 'Gana Computadora' 
    print 'Resultado:' + gana

inicia_juego()