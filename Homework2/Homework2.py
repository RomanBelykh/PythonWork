# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
# n = float(input("Введите число - "))
# while n%1>0:
#     n*10
# summ=0
# while n>0:
#     summ +=n%10
#     n //=10
# print(int(summ))

# # 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# # Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n= int(input("Введите число - "))
ans = list ()
result = 1
for i in range(n):
    result = result*(i+1)
    ans/append(result)
print(ans)
# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 5. Реализуйте алгоритм перемешивания списка.