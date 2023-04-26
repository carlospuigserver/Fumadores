import threading
import random
import time

ingredientes=["papel","tabaco","filtros","cerillas", "green"]
fumadores=["1","2","3"]


def agente():
    while True:
        ingredientesDisponibles=ingredientes.copy()
        ingrediente1=random.choice(ingredientesDisponibles)
        ingrediente2=random.choice(ingredientesDisponibles)
        print(f"El agente deja en la mesa {ingrediente1} y {ingrediente2}")
        time.sleep(1)