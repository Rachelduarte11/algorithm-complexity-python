# Busqueda Binaria

import random

def binary_search(lst, start, end, target):
    
    print(f'Buscando {target} entre {lst[start]} y {lst[end-1]}')
    if start > end:
        return False
    
    mid= (start + end) //2

    if lst[mid] == target:
        return True
    elif lst[mid] < target:
         return binary_search(lst, mid + 1, end, target)
    else:
        return binary_search(lst, start, mid-1, target)
    
    #Big O notation: O(log n)

if __name__ == '__main__':
    size_lst= int(input('¿De que tamaño es la lista? '))
    target = int(input('¿Qué número quieres encontrar? '))

    lst= sorted([random.randint(0, 100) for i in range(size_lst)])

    found= binary_search(lst, 0, len(lst), target)

    print(lst)
    print(f'El elemento {target} {"está" if found else "no está"} en la lista')
