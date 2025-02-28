import random

def merge_sort(lst):
    if len(lst) > 1:
        #Dividimos la lista en dos sublistas
        mid= len(lst) // 2
        left= lst[:mid]
        right= lst[mid:]
        print(f'left: {left} - right: {right}')

        #Hacemos la llamada recursiva para que se sigan dividiendo las sublistas
        merge_sort(left)
        merge_sort(right)

        # Creamos dos iteradores para recorrer las sublistas y otro para la lista principal
        i= 0
        j= 0
        k= 0

        #En este bloque hacemos las primeras comparaciones para ordenar la lista
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k]= left[i]
                i += 1
            else:
                lst[k]= right[j]
                j += 1
            k += 1

        #
        while i < len(left):
            lst[k]= left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k]= right[j]
            j += 1
            k += 1
        
        print(f'comparación de left: {left} - right: {right}')
        print(f'lista: {lst}')
        print('-' * 50)

    return lst


if __name__ == '__main__':
    size_lst= int(input('¿De que tamaño es la lista? '))

    lst= [random.randint(0, 100) for i in range(size_lst)]
    print(lst)

    lst_sorted= merge_sort(lst)
    print(lst_sorted)