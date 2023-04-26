import threading
import random
import time

ingredientes=["papel","tabaco","filtros","cerillas", "green"]
fumadores=["1","2","3","4","5"]


def agente():
    while True:
        ingredientesDisponibles=ingredientes.copy()
        ingrediente1=ingredientesDisponibles.pop(ingredientesDisponibles.index(random.choice(ingredientes)))
        ingrediente2=ingredientesDisponibles.pop(ingredientesDisponibles.index(random.choice(ingredientesDisponibles)))
        
        print(f"El agente deja en la mesa {ingrediente1} y {ingrediente2}")
        time.sleep(1)

def fumador(nombre, ingrediente1, ingrediente2):
    while True:
        if (ingrediente1 in ingredientes) and (ingrediente2 in ingredientes):
            ingredientes.remove(ingrediente1)
            ingredientes.remove(ingrediente2)
            print(f"Fumador {nombre} esta fumando con {ingrediente1} y {ingrediente2}")
            time.sleep(2)
            ingredientes.append(ingrediente1) 
            ingredientes.append(ingrediente2)
            print(f"Fumador {nombre} termino de fumar")
            time.sleep(1)
        else:
            print(f"El Fumador {nombre} esta esperando a que el agente defe {ingrediente1} y {ingrediente2} en la mesa")
            time.sleep(1)

