print('Задача 1: Вывести на экран циклом пять строк из нулей,'
      ' причем каждая строка должна быть пронумерована')


for i in range(6):
    i=i+1
    if i==6: break
    print(i, 'строка: ', 0)

print('Задача 2: '
      'Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5')

user= input('введите числа: ')
for i in range(11):
    i=i+1
    user+=input('введите еще числа: ')
    if i==9: break

user = int(user)
count=0
while user>0:
    if user%10 == 5:
        count= count+1
    user = user//10
print('Вы ввели цифру "5" ',count,'раз(а)')

print('Задача 3: '
'Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')

sum = 0

for i in range(1,101):
    sum+=i
print(sum)

print('Задача 4: '
'Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')

pr =1
for i in range(1,11):
    pr*=i
print(pr)

print('Задача 5: '
'Вывести цифры числа на каждой строчке.')


integer_number = 2129

#print(integer_number%10,integer_number//10)

while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10


print('Задача 6: '
'Найти сумму цифр числа.')

number = 38592
sum=0
while number>0:
    sum+=number%10
    number=number//10
print('Сумма чисел "38592" равна: ',sum)



print('Задача 7: '
'Найти произведение цифр числа.')

number = 5678
pr=1
while number>0:
    pr*=number%10
    number=number//10
print('Произведение чисел "5678" равна: ',pr)


print('Задача 8: '
'Дать ответ на вопрос: есть ли среди цифр числа 5?')

integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

print('Задача 9: '
'Найти максимальную цифру в числе')

number = 87549
max=0
while number>0:
    digit=number%10
    if digit>max:
        max=digit
    number=number//10
print('Максимальное число:',max)


print('Задача 10: '
'Найти количество цифр 5 в числе')

number=459853205879
count=0
while number>0:
    digit=number%10
    if digit==5:
        count+=1
    number=number//10
print('Цифра "5" в числе 459853205879 повторяется',count,'раза')
