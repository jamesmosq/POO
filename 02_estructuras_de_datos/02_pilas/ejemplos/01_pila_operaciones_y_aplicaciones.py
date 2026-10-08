#1.OPERACIONES BÁSICAS:

class Pila:
    def __init__(self):
        self.items = []

    # 1. PUSH - Añadir elemento
    def push(self, item):
        self.items.append(item)

    # 2. POP - Eliminar y retornar el último elemento
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    # 3. PEEK/TOP - Ver el último elemento sin eliminarlo
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # 4. IS_EMPTY - Verificar si está vacía
    def is_empty(self):
        return len(self.items) == 0

    # 5. SIZE - Obtener tamano
    def size(self):
        return len(self.items)

    # 6. CLEAR - Limpiar la pila
    def clear(self):
        self.items = []

#3.OPERACIONES ADICIONALES:
class PilaAvanzada(Pila):
    # 7. DUPLICAR el último elemento
    def duplicate_top(self):
        if not self.is_empty():
            self.push(self.peek())

    # 8. INTERCAMBIAR los dos últimos elementos
    def swap(self):
        if self.size() >= 2:
            item1 = self.pop()
            item2 = self.pop()
            self.push(item1)
            self.push(item2)

    # 9. ROTAR elementos (n posiciones)
    def rotate(self, n):
        if self.size() > 1 and n > 0:
            temp = self.items[-n:] + self.items[:-n]
            self.items = temp

    # 10. BUSCAR un elemento
    def search(self, item):
        return item in self.items

    # 11. CONTAR ocurrencias de un elemento
    def count(self, item):
        return self.items.count(item)


#4 APLICACIONES PRÁCTICAS:
# 1. Invertir una cadena
def invertir_cadena(texto):
    pila = Pila()
    # Añadir cada carácter a la pila
    for char in texto:
        pila.push(char)

    # Reconstruir la cadena invertida
    texto_invertido = ""
    while not pila.is_empty():
        texto_invertido += pila.pop()

    return texto_invertido


# 2. Verificar palíndromos
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == invertir_cadena(texto)


# 3. Convertir número decimal a cualquier base
def convertir_base(decimal, base):
    pila = Pila()
    digitos = "0123456789ABCDEF"

    while decimal > 0:
        pila.push(digitos[decimal % base])
        decimal //= base

    resultado = ""
    while not pila.is_empty():
        resultado += pila.pop()

    return resultado


# 4. Evaluar expresiones postfijas
def evaluar_postfija(expresion):
    pila = Pila()
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for token in expresion.split():
        if token in operadores:
            b = float(pila.pop())
            a = float(pila.pop())
            resultado = operadores[token](a, b)
            pila.push(str(resultado))
        else:
            pila.push(token)

    return float(pila.pop())


#5. EJEMPLOS DE USO DE APLICACIONES:
# Pruebas de las aplicaciones
print(invertir_cadena("Hola Mundo"))  # odnuM aloH
print(es_palindromo("Anita lava la tina"))  # True
print(convertir_base(255, 16))  # FF
print(evaluar_postfija("5 3 + 2 *"))  # 16


#6 VERIFICACIONES DE PILA:
def verificar_balance(expresion):
    pila = Pila()
    apertura = "({["
    cierre = ")}]"
    pares = dict(zip(cierre, apertura))

    for char in expresion:
        if char in apertura:
            pila.push(char)
        elif char in cierre:
            if pila.is_empty():
                return False
            if pila.pop() != pares[char]:
                return False

    return pila.is_empty()


# Ejemplo de uso
print(verificar_balance("{[()]}"))  # True
print(verificar_balance("{[(])}"))  # False
