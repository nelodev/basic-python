# contador = 0
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 1
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 2
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 3
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 4
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# contador = 5
# print("2 elevado a " + str(contador) + " es igual a: " + str(2**contador))

# WHILE LOOP
def runWhile():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador = contador+1
        potencia_2 = 2**contador

# FOR LOOP
def runFor():
    # for contador in range(2, 10):
    #     print(contador)

    # for i in range(10):
    #     print(11*i)

    # nombre = input("Escribe tu nombre: ")
    # for letra in nombre:
    #     print(letra)

    # frase = input("Escribe una frase: ")
    # for caracter in frase:
    #     print(caracter.upper())

    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break;

    texto = input("Escribe una frase: ")
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == "__main__":
    # runWhile()
    runFor()
