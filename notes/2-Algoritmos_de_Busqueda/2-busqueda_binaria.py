# Busqueda Binaria
# La busqueda binaria es un algoritmo de búsqueda de un elemento en una lista ordenada.

# ¿Cómo funciona?
# Se divide el arreglo en dos mitades y se compara el elemento buscado con el elemento en el medio.

# ¿Cual es el peor caso?
# El peor caso es cuando el elemento que se busca no está en la lista.

import random
import time

def binary_search(lst, start, end, target, contador):
    contador[0] += 1  # Incrementa el contador de iteraciones
    print(f'Iteración {contador[0]}: Buscando {target} entre {lst[start]} y {lst[end-1] if end-1 < len(lst) else "fuera del rango"}')

    if start > end:
        return False
    
    mid= (start + end) //2

    if lst[mid] == target:
        return True
    elif lst[mid] < target:
         return binary_search(lst, mid + 1, end, target, contador)
    else:
        return binary_search(lst, start, mid-1, target, contador)
    
    #Big O notation: O(log n)

if __name__ == '__main__':
    size_lst= int(input('¿De que tamaño es la lista? '))
    target = int(input('¿Qué número quieres encontrar? '))

    lst= sorted([random.randint(0, 100) for i in range(size_lst)])

    contador = [0]  # Usamos una lista para que el contador sea mutable

    start_time = time.time()  # Inicia el cronómetro
    found = binary_search(lst, 0, len(lst) - 1, target, contador)
    end_time = time.time()  # Detiene el cronómetro

    print(lst)
    print(f'El elemento {target} {"está" if found else "no está"} en la lista')
    print(f'Tiempo de ejecución: {end_time - start_time:.6f} segundos')
    print(f'Número de iteraciones: {contador[0]}')
