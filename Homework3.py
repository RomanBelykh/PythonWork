# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# 
#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# inp = list(map(int, input('Введите число - ').split()))
# ans = list ()
# for i in range(len(inp)//2):
#    ans.append(inp[i]* inp[len(inp) -i -1])
# if len(inp)% 2 == 1:
#    ans.append(inp[int(len(inp)/2)]**2)
# print(*ans)

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# inp = list(map(float, input('Введите число - ').split()))
# ans = list()
# for i in inp:
#    x= i - int(i)
#    if x !=0:
#       ans.append(round(x, 5))
# if max(ans) == min(ans):
#    print (max(ans))
# else:
#    print(max(ans) - min(ans))

#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def BinaryCode (number):
#    ans = list()
#    rest = number% 2
#    rez = number// 2
#    ans.append(rest)
#    while rez !=0:
#       rest = rez % 2
#       rez = rez// 2
#       ans.append(rest)
#    ans.reverse
#    return ans

# N = int(input('Введите число - '))
# answer = BinaryCode(N)
# print(N, ' в двоичном коде - ', *answer, sep ='')

#Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def Fibonacci(number):
#    if number ==1 or number ==2:
#       return 1
#    else:
#       return Fibonacci(number-1) + Fibonacci(number-2)
# N = int(input('Введите чило - '))
# ans = list ()
# for i in range(1, N+1):
#    ans.append(Fibonacci(i)*((-1)**(i+1)))
# ans.reverse()
# ans.append(0)
# for i in range(1, N+1):
#        ans.append(Fibonacci(i))
# print(*ans)
 #Эту задачу я подсмотрел