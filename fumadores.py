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
        time.sleep(3)

def fumador(nombre, ingrediente1, ingrediente2):
    while True:
        if (ingrediente1 in ingredientes) and (ingrediente2 in ingredientes):
            ingredientes.remove(ingrediente1)
            ingredientes.remove(ingrediente2)
            print(f"Fumador {nombre} esta fumando con {ingrediente1} y {ingrediente2}")
            time.sleep(4)
            ingredientes.append(ingrediente1) 
            ingredientes.append(ingrediente2)
            print(f"Fumador {nombre} termino de fumar")
            time.sleep(3)
        else:
            print(f"El Fumador {nombre} esta esperando a que el agente defe {ingrediente1} y {ingrediente2} en la mesa")
            time.sleep(3)

hiloAgente=threading.Thread(target=agente)
hiloFumador1=threading.Thread(target=fumador, args=("1","papel","tabaco"))
hiloFumador2=threading.Thread(target=fumador, args=("2","papel","cerillas"))
hiloFumador3=threading.Thread(target=fumador, args=("3","tabaco","cerillas"))
hiloFumador4=threading.Thread(target=fumador, args=("4","green","filtros"))
hiloFumador5=threading.Thread(target=fumador, args=("5","green","cerillas"))

hiloAgente.start()
hiloFumador1.start()
hiloFumador2.start()
hiloFumador3.start()
hiloFumador4.start()
hiloFumador5.start()

hiloAgente.join()
hiloFumador1.join()
hiloFumador2.join()
hiloFumador3.join()
hiloFumador4.join()
hiloFumador5.join()

