#Llenar una lista con palabras hasta que se ingrese una palabra vacía:

palabras = []
while True:
    palabra = input("Ingrese una palabra (o presione Enter para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)

for i in palabras:
        print(f" organmizados con un for {i}")

#print("Lista de palabras:", palabras)