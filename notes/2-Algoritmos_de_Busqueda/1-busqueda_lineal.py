# Búsqueda Lineal
# La búsqueda lineal es el método más sencillo de búsqueda de un elemento en una lista.

#¿Cómo funciona?
# Se recorre la lista de principio a fin, comparando cada elemento con el valor que se busca.

# ¿Cual es el peor caso?
# El peor caso es cuando el elemento que se busca es el último de la lista o no está en la lista.

###############################################################################################################

# Esta es una implementación de la búsqueda lineal en Python:
# Nos da como resultado una complejidad lineal, ya que el tiempo de ejecución crece de 
# manera lineal con el tamaño de la lista.

import random

def linear_search(lst, target):
    match= False

    for elemento in lst:
        if elemento == target:
            match = True
            break

    return match

    #Big O notation: O(n)

if __name__ == '__main__':
    size_lst= int(input('¿De que tamaño es la lista? '))
    target = int(input('¿Qué número quieres encontrar? '))

    lst= [random.randint(0, 100) for i in range(size_lst)]

    found= linear_search(lst, target)
    print(lst)
    print(f'El elemento {target} {"está" if linear_search(lst, target) else "no está"} en la lista')

# Es lineal porque solo tenemos un loop que recorre la lista una vez.