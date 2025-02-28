{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import random\n",
    "\n",
    "def bubble_sort(arr):\n",
    "    n = len(arr)\n",
    "    for i in range(n):\n",
    "        for j in range(0, n - i - 1):\n",
    "            if arr[j] > arr[j + 1]:\n",
    "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n",
    "    return arr\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    size_lst= int(input('¿De que tamaño es la lista? '))\n",
    "\n",
    "    lst= [random.randint(0, 100) for i in range(size_lst)]\n",
    "    print(lst)\n",
    "\n",
    "    lst_sorted= bubble_sort(lst)\n",
    "    print(lst_sorted)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
