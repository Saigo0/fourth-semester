def prefixo (lista):
    prefix = ""
    maiorPrefixo = ""
    lista.sort()
    string1 = lista[0]
    string2 = lista[-1]

    for i in range (len(lista)):
        prefix += string1[i]

    for i in range (len(prefix)):
        if prefix[i] == string2[i]:
            maiorPrefixo += prefix[i]


    return maiorPrefixo


list1 = ["corsa", "cor", "corante"]
print("Maior prefixo comum: ", prefixo(list1))



