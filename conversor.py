def conversor(type, dolar_value):
    pesos = input("How many " + type + " pesos do you have?: ")
    pesos = float(pesos)
    dolares = pesos / dolar_value
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("You have $" + dolares + " dollars")

menu = """
Welcome to the LATAM pesos converter 💰

1 - Colombian pesos
2 - Argentinian pesos
3 - Mexican pesos

Choose an option: """

option = input(menu)

if option == '1':
    conversor("colombian", 387)
elif option == '2':
    conversor("argentinian", 65)
elif option == '3':
    conversor("mexican", 24)
else:
    print("Choose a valid option, please")
