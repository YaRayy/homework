print('Введите три числа')
a=int(input())
b=int(input())
c=int(input())
if b<a>c or c<a>b:
    print('Среднее значение' ,a)
elif a<b>c or c<b>a:
    print('Среднее значение' ,b)
elif a<c>b or b<c>a;
    print('Среднее значение' ,c)
else:
   print('Error input')
print('Successed')
