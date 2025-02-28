
def morral(size_morral, weights, vals, n):
    #Caso base
    if n == 0 or size_morral == 0:
        return 0
    
    if weights [n-1] > size_morral:
        print("Peso mayor al morral, no se puede agregar")
        return morral(size_morral, weights, vals, n-1)
    
    return max(vals[n-1] + morral(size_morral-weights[n-1], weights, vals, n-1), 
               morral(size_morral, weights, vals, n-1))
    


#Entry point
if __name__ == '__main__':
    vals= [60, 100, 120]
    weights= [10, 20, 30]
    size_morral= 20
    n= len(vals)

    result= morral(size_morral, weights, vals, n)
    print(result)