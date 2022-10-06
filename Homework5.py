#Задача1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from encordings import utf_8

with open ("words.txt", encording='utf_8') as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if 'абв' in word:
                words.remove(word)
        sentence = "".join(words)
        print(sentence)

# Задача2.Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

print(
    '"Игра с конфетами: на столе лежит 2021 конфета,\n'
    'играют два игрока делая ход друг после друга.\n'
    'Первый ход определяется жеребьёвкой.\n'
    'За один ход можно забрать не более чем 28 конфет.\n'
    'Все конфеты оппонента достаются сделавшему последний ход.\n'
)

player1 = input('Первый игрок, введите Ваше имя:\n')
player2 = input('Второй игрок, введите Ваше имя: \n')
players = [player1, player2]

total_sweets = 2021
max_number_move = 28

# print(total_sweets % max_number_move)

def game_friend_vs_friend_or_smartbot(total_sweets, max_number_move, players):
    count = 0
    first = random.randint(0, 1)
    print (f'\nПервый ход определён жеребьёвкой, начинает игрок № {first + 1}')
    while total_sweets > 0:
        if players[0] == 'бот' and first % 2 == 0:
            if total_sweets > 28:
                move = total_sweets % (max_number_move + 1)
            else:
                move = total_sweets
        elif players[1] == 'бот' and first % 2 == 1:
            if total_sweets > 28:
                move = total_sweets % (max_number_move + 1)
            else:
                move = total_sweets
        else:
            move = int(input(f'{players[first % 2]}: '))
        if move > total_sweets or move > max_number_move:
            print(f'Можно взять не более 28 конфет, у нас всего {total_sweets} конфет(ы)!')
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                if players[0] == 'бот' and first % 2 == 0:
                    if total_sweets > 28:
                        move = total_sweets % (max_number_move + 1)
                    else:
                        move = total_sweets
                elif players[1] == 'бот' and first % 2 == 1:
                    if total_sweets > 28:
                        move = total_sweets % (max_number_move + 1)
                    else:
                        move = total_sweets
                else:
                    move = int(input())
                chance -= 1
            else:
                return print(f'Попытки закончились! Вы проиграли!')
        total_sweets = total_sweets - move
        if total_sweets > 0:
            print(f'Осталось {total_sweets} конфет(ы)!')
        else:
            print('Все конфеты разобраны.')
        first += 1
    return players[(first - 1) % 2]

def game_friend_vs_friend_or_fullbot(total_sweets, max_number_move, players):
    count = 0
    first = random.randint(0, 1)
    print (f'\nПервый ход определён жеребьёвкой, начинает игрок № {first + 1}')
    while total_sweets > 0:
        if players[0] == 'бот' and first % 2 == 0:
            move = random.randint(0, 28)
        elif players[1] == 'бот' and first % 2 == 1:
            move = random.randint(0, 28)
        else:
            move = int(input(f'{players[first % 2]}: '))
        if move > total_sweets or move > max_number_move:
            print(f'Можно взять не более 28 конфет, у нас всего {total_sweets} конфет(ы)!')
            chance = 2
            while chance > 0:
                if total_sweets >= move <= max_number_move:
                    break
                print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                if players[0] == 'бот' and first % 2 == 0:
                    move = random.randint(0, 28)
                elif players[1] == 'бот' and first % 2 == 1:
                    move = random.randint(0, 28)
                else:
                    move = int(input())
                chance -= 1
            else:
                return print(f'Попытки закончились! Вы проиграли!')
        total_sweets = total_sweets - move
        if total_sweets > 0:
            print(f'Осталось {total_sweets} конфет(ы)!')
        else:
            print('Все конфеты разобраны.')
        first += 1
    return players[(first - 1) % 2]

winer = game_friend_vs_friend_or_smartbot(total_sweets, max_number_move, players)
if not winer:
    print('Победителя нет.')
else:
    print(f'Поздравляю! Победил {winer}!')

# Задача3.Создайте программу для игры в "Крестики-нолики".

print("*" * 10, " Игра Крестики-нолики ", "*" * 10)

board = list(range(1,10))

def draw_board(board): # заполняет поле построчно
    print("-" * 13) # первая горизонтальная линия
    for i in range(3): # проходим по трем строчкам 
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|") #  с каждым проходом строчки мы выводим число из списка по порядку по три столбика по позициям чисел в списке
        print("-" * 13) # выводит линию после каждого прохода по строчке, т.е. три линии

def take_input(player_token): #  заполнение ячеек в поле
    valid = False
    while not valid: # цикл заполнения если нет ошибки
        player_answer = input("Куда поставим " + player_token+"? ") # спрашиевает в зависимости от игрока ставить Х или О
        try:
            player_answer = int(player_answer) # принимает на вход число в клетке поля куда поставить Х или О
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?") #  проверка на ввод целого числа, а не символа или натурального числа
            continue
        if player_answer >= 1 and player_answer <= 9: # если введено целое число, то проверка на ввод числа от 1 до 9
            if(str(board[player_answer-1]) not in "XO"): # проверка не заполнена ли клетка Х или О
                board[player_answer-1] = player_token # если в поле не Х или О, то в список на позицию числа (число - 1) ставится Х или О
                valid = True # для проверки на правильность ввода
            else:
                print("Эта клетка уже занята!") # выводит если всё верно
        else:
            print("Некорректный ввод. Введите число от 1 до 9.") #  выводит если ошибка в вводе

def check_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # кортеж кортежей со всеми выйгрышными комбинациями
    for each in win_coord: # перебор кортежа
        if board[each[0]] == board[each[1]] == board[each[2]]: # если символы во всех трех заданных клетках равны - возвращаем выигрышный символ, иначе - возвращаем значение False
            return board[each[0]] # если верно
    return False # если неверно

def main(board): # компилятор игры
    counter = 0 # счетчик
    win = False 
    while not win: # цикл до победы
        draw_board(board) # вызов игрового поля
        if counter % 2 == 0: # передача хода от игрока к игроку до строки 47
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4: # до 4 ходов никто выйграть не может, после этого проверка на выйгрыш
            tmp = check_win(board) # вызов метода проверки выйгрышных комбинаций
            if tmp: # условие вывода выйгрыша
                print(tmp, "выиграл!") 
                win = True # для остановки цикла while
                break 
        if counter == 9: # если полностью закрыты все клетки, и нет победтеля то выводит Ничья!
            print("Ничья!")
            break
    draw_board(board)
main(board) # вызов компилятора

input("Нажмите Enter для выхода!")  # остановка программы

# все решения это задачи есть в интернете, но чтобы показать, 
# что полностью разобрался и понял, откоментировал каждую строку!

# Задача 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_for_numbers(data): # для чисел, но для этого метода не придумал как восстанавливать. Ну и тут просто вывод на экран.
    string = ''
    cout = 1
    for i in range(len(string)-1):
        if i <= len(string):
            if string[i] == string[i + 1]:
                cout += 1
            else:
                a = string[i]
                print(cout, string[i])
                cout = 1
    print(cout, string[i])

def rle_encode(data): # сжатие для любых символов, но некорректно будет работать с числами
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data): # восстановление для любых символов, кромы цифр
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open("RLEencode.txt", "r") as enterFile:
    enterData = enterFile.readline()
print(f'Ваша запись во входящем файле: {enterData}')

encoded_val = rle_encode(enterData) 
print(f'Ваша запись после RLE-сжатия: {encoded_val}')

decoded_val = rle_decode(encoded_val)
print(f'Ваша запись после RLE-восстановления: {decoded_val}')

with open("RLEdecode.txt", "w") as exitFile:
    exitFile.write(decoded_val)

enterFile.close()
exitFile.close()

# смысл сжатия и восстановления проработал, сейчас к сожалению из за работы мало врмени, 
# поэтому если будет время подумаю как модернизировать для любых символов, 
# думаю через список кортежей или список списков.

# def Compression(text): #алгоритм сжатия
#     compresdata = ''

#     i = 0
#     while i < len(text):
#         count = 1
#         while i + 1 < len(text) and text[i] == text[i + 1]:
#             count += 1
#             i += 1
#         compresdata += str(count) + text[i]
#         i += 1
    
#     return compresdata


# def Recovery(text): #алгоритм восстановления
#     datarecovery = ''

#     i = 0
#     while i < len(text):
#         datarecovery += str(text[i+1]) * int(text[i])
#         i+=2
    
#     return datarecovery


# with open('Text1.txt', 'r') as t1:
#     t1 = t1.read()    

# with open('Text2.txt', 'w+') as t2:
#     t2.write(Compression(t1))
#     t2.seek(0)                     #возврат курсора на начало строки
#     t2 = t2.read()
 
# with open('Text3.txt', 'w') as t3:
#     t3.write(Recovery(t2))