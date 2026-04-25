#Remover elementos de un set mientras no esté vacío
numeros = {1,8,"hola"}
while numeros:
    elemento = numeros.pop()
    print(f"Removido: {elemento}")
    print(numeros)
print("Set vacío:", numeros)