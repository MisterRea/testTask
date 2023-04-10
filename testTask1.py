a = input('Введите число ')
a = int(a)
b = a.to_bytes(2,byteorder='little')
print('Результат:',int.from_bytes(b,'big'))