
a = 1, 2, 3
b = str(a)
print(b)
print(type(b))

a = 1, 5.5, "hello"
b = list(a)
print(b)
print(type(b))

a = str(input('Введите строку: '))
b = len(a)
print(f'Количество символов в строке: {b}')