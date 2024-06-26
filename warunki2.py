# od pythona 3.10
# match case

lista = []
lang = input('Podaj znany ci język programowania')

match lang.lower().replace(" ", ""):
    case "python":
        lista.append("Python")
    case "java":
        lista.append("Java")
    case _:  # wartość domyslna
        print("Nie znam takiego języka")

print(lista)
