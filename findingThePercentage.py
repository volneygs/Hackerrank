def findingThePercentage(lista, nome):

    for i in range(len(lista)):
        if(lista[i][0] == nome):
            resposta = porcentagem(lista[i])

    return resposta

def porcentagem(lista):

    soma = float(lista[1]) + float(lista[2]) + float(lista[3])

    porcentagem = soma/(len(lista)-1)

    return porcentagem


num = int(input())

lista = []

for i in range(num):

    lista.append(list(map(str, input().split())))

nome = input()

print("%.2f" % (findingThePercentage(lista, nome)))