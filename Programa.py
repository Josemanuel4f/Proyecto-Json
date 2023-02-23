from Funciones import *

opcion = menu()
while opcion > 0 and opcion < 6:
    if opcion == 1:
        mostrarkiwi()
    if opcion == 2:
        cantidadkiwi()
    if opcion == 3:
        subcadena()
    opcion = menu()