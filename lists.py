def listas():

    n = int(input())

    lista = []

    for i in range(n):
        
        req = list(map(str, input().split()))

        entrada = req[0]

        if(entrada == "insert"):

            position = int(req[1])
            num = int(req[2])

            lista.insert(position, num)
        
        elif(entrada == "print"):

            print(lista)

        elif(entrada == "remove"):

            num = int(req[1])

            lista.remove(num)

        elif(entrada == "append"):

            lista.append(int(req[1]))

        elif(entrada == "sort"):

            lista.sort()

        elif(entrada == "pop"):

            lista.pop()
        
        elif(entrada == "reverse"):

            lista.reverse()
    
    return True

listas()