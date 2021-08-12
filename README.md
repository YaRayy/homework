print('Введите три числа:')
a = int(input())
b = int(input())
c = int(input())
if a > b and a < c:
	print(a, 'Среднее значение')
elif a < b and a > c:
	print(a, 'Среднее значение')
elif b > a and b < c:
	print(b, 'Среднее значение')
elif b < a and b > c:
	print(b, 'Среднее значение')
elif c > a and c < b:
	print(c, 'Среднее значение')
elif c < a and c > b:
	print(c, 'Среднее значение')
else:
	print('Incorrect indicate')
print('Successed')
