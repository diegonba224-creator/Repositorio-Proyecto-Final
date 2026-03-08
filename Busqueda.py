import os    # Se importa la libreria os
def limpiar_terminal():    # Se crea la funcion limpar_terminal
        os.system("cls")    # Ejecuto el comando cls
limpiar_terminal()       # Llamo la funcion creada

def busqueda_binaria(elementos, x):
    """
    Implementa búsqueda binaria en una lista ordenada.
    """
    # PRIMERO debemos ordenar la lista (requisito de la búsqueda binaria)
    elementos_ordenados = sorted(elementos)                          # Ordeno la lista de elementos ascendentemente
    print("📊 Lista ordenada para la búsqueda:", elementos_ordenados)
    
    izquierda = 0                                      # Índice inicial de la lista 
    derecha = len(elementos_ordenados) - 1             # Índice final de la lista 
    posicion_original = -1                             # Para guardar la posición en la lista original 
    
    while izquierda <= derecha:                        # Mientras el índice izquierdo no supere al derecho
        medio = (izquierda + derecha) // 2             # Calculo el índice del elemento medio 
        
        print(f"🔍 Buscando... izquierda={izquierda}, derecha={derecha}, medio={medio}, valor={elementos_ordenados[medio]}") 
        
        if elementos_ordenados[medio] == x:            # si el elemento medio es igual al valor buscado:
            # Encontramos el elemento, ahora buscamos su posición en la lista original
            for i in range(len(elementos)):
                if elementos[i] == x:                  # si el elemento en la posición i es igual a x:
                    break                              # Salimos del bucle for 
            return True, posicion_original, elementos_ordenados  # Retornamos True, la posición y la lista ordenada 
        elif elementos_ordenados[medio] < x:           # Si el elemento medio es menor que el valor buscado:
            izquierda = medio + 1                      # Buscar en la mitad derecha 
        else:                                          # Si el elemento medio es mayor que el valor buscado:
            derecha = medio - 1                        # Buscar en la mitad izquierda 
    
    return False, -1, elementos_ordenados              # Si no se encuentra, retornamos False, -1 y la lista ordenada

# Programa principal
elementos = [5, 7, 10, 12, 15, 60, 69, 98, 90, 24, 35, 33, 11]  # Defino la lista de elementos

print("📝 La lista original de elementos es:", elementos)  # Muestro la lista de elementos
print(40*"-")  # Imprimo un separador para visualizar mejor la salida
x = int(input("Ingrese el elemento a buscar: "))  # Solicito el elemento a buscar y lo convierto a entero

# Realizar búsqueda binaria
encontrado, posicion, lista_ordenada = busqueda_binaria(elementos, x)

print(40*"-")
if encontrado:                                         # Verifico si se encontró el elemento 
    print(f"🎯 Elemento {x} encontrado:")              # muestr
    print(f"   • Posición en lista original: {posicion + 1}") # (sumo 1 porque los índices empiezan en 0) 
    print(f"   • Posición en lista ordenada: {lista_ordenada.index(x) + 1}") # (sumo 1 porque los índices empiezan en 0)
    print(f"   • Lista ordenada: {lista_ordenada}")        # Muestro la lista ordenada 
else:                                                      # Si no se encontró el elemento:
    print(f"❌ Elemento {x} no encontrado en la lista")    # Indico que no se encontró el elemento 
print(40*"-")                                              
# Descripción básica de la funcionalidad del código
