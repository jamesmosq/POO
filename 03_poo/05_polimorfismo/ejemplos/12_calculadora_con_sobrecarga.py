# Ejercicio 1: Calculadora avanzada
class Calculadora:
    def sumar(self, a, b=None, *args):
        if b is None:
            return a
        total = a + b
        for num in args:
            total += num
        return total

# Uso:
calc = Calculadora()
print(calc.sumar(5))          # 5
print(calc.sumar(0, 3))       # 8
print(calc.sumar(5, 3, 2, 1)) # 11

