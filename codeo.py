n = int(input())
m = list(map(int, input().split()))
def calcular_mayor(lista):
    posicion = 0
    numero_mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > numero_mayor:
            numero_mayor = lista[i]
            posicion = i
    print(numero_mayor, posicion)
calcular_mayor(m)

