# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# # *Пример:*

# 385916 -> yes
# 123456 -> no

print ('введите шестизначное число')
number = int (input())

a1 = number % 10
number = number // 10
a2 = number % 10
number = number // 10
a3 = number % 10
number = number // 10
a4 = number % 10
number = number // 10
a5 = number % 10
number = number // 10
a6 = number % 10
number = number // 10
sum1 = a1 + a2 + a3
sum2 = a4 + a5 + a6

if (sum1 == sum2):
    print ("Тебе повезло,билет счастливый, удача на твоей стороне")
else:
    print ("Увы тебе не повезло")
