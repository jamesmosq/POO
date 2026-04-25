class Person:
    def __init__(self, name, age, email,phone, favorite_food):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.favorite_food = favorite_food

p1 = Person("John", 36, "John@example.com", "6564541", "eyryrry")
p2 = Person("Ana", 10, "Ana@example.com", "965476514","ghhhffh")
p3 = Person("Ana", 10, "Ana@example.com", "","")

print(p1.name, p1.age, p1.email, p1.phone)
print(p2.name, p2.age)
print(p3.name, p3.age, p3.email, p3.phone)

