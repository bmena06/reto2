def bubblesort(lista):   
    n = 0 
    for _ in lista:
        n += 1
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print ("El vector ordenado con el metodo bubblesort es: ", lista)

def selectionsort(lista):
    largo = 0 
    for _ in lista:
        largo += 1 
        
    for i in range(largo): 
        minimo = i 
        for j in range(i+1, largo): 
            if lista[minimo] > lista[j]: 
                minimo = j 
        lista[i], lista[minimo] = lista[minimo], lista[i]
    print("El vector ordenado con el metodo selección es: ",lista)

def validar_entero():
    while True:
        cantidad = input("Ingrese la cantidad de números que desea: ")
        try:
            cantidad=int(cantidad)
            return cantidad
        except ValueError:
            print("El número debe ser entero.")

numeros = []
cantidad=validar_entero()
while len(numeros) < cantidad:
    numero = input("Ingrese un número: ")
    if not numero.isdigit():
        print("El número debe ser entero.")
    else:
        numeros.append(int(numero))

print("El vector sin ordenar es: ",numeros)
bubblesort(numeros)
selectionsort(numeros)

print("El numero mayor es: ",numeros[0])
print("El numero menor es: ",numeros[-1])