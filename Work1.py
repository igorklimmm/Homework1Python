# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print ('введите трехзначное число')
number = int (input())

if (number > 1000 | number < 100):
 print('ошибка, введите ТРЕХЗНАЧНОЕ число') 
 # Не получается сделать проверку на то что является число трех значным или нет, по возможности напишите как это сделать.

if (number < 1000 | number > 100):
  a1 = number % 10
  number = number // 10
  a2 = number % 10
  number = number // 10
  print ('Cумма чисел равна' , number + a1 + a2)

