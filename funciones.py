# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("¡Estoy aprendiendo a usar funciones!")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# def conversacion(opcion):
#     print("Hola")
#     print("¿Cómo estás?")
#     print("Elegiste la opción " + str(opcion))
#     print("Adiós")

# opcion = int(input('Elige una opción (1, 2, 3): '))
# conversacion(opcion)

def suma(a, b):
    print('Se suman dos números, ' + str(a) + " y " + str(b))
    resultado = a+b
    return resultado

sumatoria = suma(1,4)
print("Resultado: " + str(sumatoria))
