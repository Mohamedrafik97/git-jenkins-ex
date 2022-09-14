class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Shop:
    def __init__(self, x, y):
        self.x = x
        self.y = y


s1 = Shop('3', "big")
s2 = Shop('5', 'small')
p1 = Person("JOHN", 36)

print(p1.name)
print(p1.age)
print(s1.y)
print(s1.x)
print(s2.x, s2.y)
