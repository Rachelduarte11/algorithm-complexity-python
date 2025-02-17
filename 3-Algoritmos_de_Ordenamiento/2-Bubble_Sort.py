
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    size_lst= int(input('¿De que tamaño es la lista? '))

    lst= [random.randint(0, 100) for i in range(size_lst)]
    print(lst)

    lst_sorted= bubble_sort(lst)
    print(lst_sorted)
