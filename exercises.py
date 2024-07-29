"""
exercises
author:Natalia
"""

height = int(input("Введите высоту: "))
while height<1: height = int(input("Введите высоту боше нуля: "))

branch = "*"
space = " " * max((height - 1),0)
for i in range (0, height):
    print(space+branch)
    branch = "*" + branch + "*"
    space = space[0:-1]

#new

lst = [100, 12, 2, 33, 4, 10, 100, 21, 90, 99, 100, -10]
max_i = []
#max_el = sorted(lst, reverse=True)[0]
max_el = max(lst)

for index, value in enumerate(lst):
    if value == max_el:
        max_i.append(index)

print(max_i)

# new

"""
игра угадай число
author:Natalia
"""
import random
print("""Игра Угадай Целое Число""")
#Constants declaration
UPPER_RANGE = 0
RANDOM_NUMBER = 0

#variables declaration
guess_count = 0
#the secret number might be =0, to create a loop that takes only number >=0 we need -0.5 value
guess = -0.5

#Ask user to input the guessing range
while not UPPER_RANGE:
    try:
        UPPER_RANGE = int(input("Выберите верхнюю границу (>0): "))
    except ValueError:
        print("Играют только целые числа, введите целое число!")
    if UPPER_RANGE < 1:
        UPPER_RANGE = 0

#Defining the number to guess
random_number = random.randint(0, UPPER_RANGE)
print("Число загадано в диапазоне от 0 до ", UPPER_RANGE, " Угадаешь?")

#Ask user to guess the number until he finds the correct answer
while guess != random_number:
    while guess < 0:
        try:
            guess = int(input("Я думаю, что это число: "))
        except ValueError:
            print("Играют только целые числа, введите целое число!")

#count the number of attempts to guess
        guess_count += 1

        if guess < -0.5:
            print("Играют только числа >=0, введите число")

    if guess > random_number:
        print("Число больше чем загаданное.")

    elif guess < random_number:
        print("Число Меньше чем загаданное.")

    else :
        break

    guess = -0.5

print("Молодец. Твой результат: ", guess_count)

# new
def split_list(some_list: list, divider):
    el_exists = False

    if type(some_list) != list:
        return("Это не список")

    try:
        el_index = some_list.index(divider)
        el_exists = True
    except ValueError:
            return some_list

    if el_exists and el_index > 0:
        return (some_list[0:el_index], some_list[(el_index+1):len(some_list)])
    elif el_exists and el_index == 0:
        return ([], some_list[1:len(some_list)])
    else:
        return some_list

# new
"""
author:Natalia

IP адрес?
В этом задании вам предстоит самостоятельно познакомиться с правилами
формирования IP адресов версии v4 и реализовать функцию is_ip(string)
которая отвечает на вопрос "Является ли переданная строка корректным
IP адресом или нет?". Функция должна вернуть True если строка является
 валидным IP адресом или False если нет."""

def is_ip(string: str):
    # Напишите ваш код здесь
    str_split = string.split(".")
    if len(str_split) !=4:
        return False
    for el in str_split:
        try:
            int_element = int(el)
        except ValueError:
            return False
        if int_element < 0 or int_element > 255:
            return False
    return True

print(is_ip("123.000.-111.2"))

"""
author:Natalia

В этом задании нужно реализовать функцию reverse_number которая принимает на вход число
и переворачивает его. Важно учитывать что отрицательные числа при этом должны оставаться
отрицательными, а положительные положительными. Если передано число типа float, то нужно
перевернуть каждую его часть отдельно, не меняя их местами. Функция должна возвращать число
того типа которое было передано.

Примеры:

reverse_number(123) -> 321
reverse_number(-100) -> -1
reverse_number(123.001) -> 321.1"""

def reverse_number(number):
    if type(number) not in [float, int]:
        return "It is not a number"

    result = 0
    negatif = 1
    if number < 0:
        negatif *= -1
        number *= -1

    if type(number) == int:
        list_number = list(str(number))
        list_number.reverse()
        string_number = ""
        for el in list_number:
            string_number += el
        result = int(string_number)

    if type(number) == float:
        string_number_all = str(number)
        list_number_all = string_number_all.split(".")
        int_part_list = list(list_number_all[0])
        float_part_list = list(list_number_all[1])
        int_part_list.reverse()
        float_part_list.reverse()
        string_number_i = ""
        for el in int_part_list:
            string_number_i += el
        string_number_f = ""
        for el in float_part_list:
            string_number_f += el
        string_number = string_number_i + "." + string_number_f
        result = float(string_number)

    return result*negatif

print(reverse_number(-1-2))


"""
author:Natalia

Кумулятивная сумма списка
В этом задании нужно реализовать функцию running_sum(some_list), которая возвращает
кумулятивную сумму списка, это когда к каждому следующему элементу мы добавляем все
предыдущие.

Пример 1

running_sum([1,1,1,1,1]) -> [1,2,3,4,5]
Как получили: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Пример 2:

running_sum([1,2,3,4]) -> [1,3,6,10]
Как получили: [1, 1+2, 1+2+3, 1+2+3+4]
Доп. требования:

1) Если в функцию передали не список, то вернуть строку "Это не список"

2) Обрабатывать списки любой длины, если список пустой или из одного элемента то вернуть сам список.

3) Если не все элементы списка типа int или float флоат, то вернуть сообщение "Плохой список"""

def running_sum(some_list: list):
    #declaration working vars
    sum = 0
    result = []
    # testing if the argument is a list
    if type(some_list) != list:
        return "Это не список"
    #testing if the argument is nothing else but int or float
    for el in some_list:
        if (type(el) != int) and (type(el) != float):
            return "Плохой список"
    #if the list is too short - nothing to do
    if len(some_list) <= 1:
        return some_list
    #calculate new list with sums
    for el in some_list:
        sum += el
        result.append(sum)
    return result

print(running_sum([3, 3]))

#new

"""
author:Natalia

В этом задании нужно реализовать функцию unzip_list(zipped_list: list) которая будет распаковывать
список элементов по следующему алгоритму и возвращать результат в качестве списка элементов.

В запакованном списке хранятся элементы следующего вида "3|4" где первое число это количество
повторений, а второе это число которое нужно повторить. Таким образом элемент вида"3|4" будет
распакован в последовательность чисел 4, 4, 4.

Все эти последовательности нужно распаковать в один список.

Пример 1

На вход: ["1|2", "3|4"]
На выходе: [2,4,4,4]
Пример 2

На вход: ["1|4", "2|5", "10|1"]
На выходе: [4,5,5,1,1,1,1,1,1,1,1,1,1]
Требования.

1) Если какой-то из элементов не содержит | но приводится к числу, то просто добавлять его
числовое представление.

Пример 3

На вход: ["1|4", "2"]
На выходе: [4, 2]"""

def unzip_list(zipped_list: list):
    # Пишите ваш код здесь
    # declaration of working variables
    result = []
    tmp = []
    # testing if the argument is a list
    if type(zipped_list) != list:
        return []

    for el in zipped_list:
        #if elemt is a string we can try to split it
        if type(el) == str:
            tmp = el.split("|")
        #if there are no separator or more than one separator in the string - cannot work with this elemet
            if len(tmp) > 2:
                return []
            elif len(tmp) == 1:
                try:
                    number = int(tmp[0])
                except ValueError:
                    return []
                result.append(number)
            else:
        #we try to unpack the number into integer
                try:
                    number = int(tmp[1])
                except ValueError:
                    return []
            # we try to unpack the number of repeats into integer
                try:
                    repeat = int(tmp[0])
                except ValueError:
                    return []

                for i in range(0, repeat):
                    result.append(number)
        else:
            try:
                result.append(int(el))
            except ValueError:
                return []
    return result
print(unzip_list(["4", 5, 1]))

#new
"""
author:Natalia

В этом заданнии будем реализовывать функцию zip_list(some_list: list) архивировать список в котором есть повторяющиеся
элементы.

Пример 1

На вход: [0,1,1,1,2,3,3,4,4,4,4]
На выходе: "0:3|1:2:2|3:4|4"
Пример 2

На вход: [0,1,2,3,4]
На выходе: "0:1:2:3:4"
Архивируются только элементы которые идет в ряд друг за другом.
Если элемент один, то просто записываем его, так как архивация его будет занимать больше места чем он сам.
Каждую заархивированную последовательность записываем в формате 3|1 где 3 это количество повторений, а 1
это число которое повторяется.
Все последовательности объединяем в строку и записываем через ":".
Если список пустой, то вернуть ":"."""

def zip_list(some_list: list):
    #declaration of working variables
    repeat_counter = 0 # to count how many times element repeats
    current_el = None #remembering previous element to check  whether series continues
    result = "" # resulting string
    index =  0 #to track the last element
    #if argument is not a list or an empty list - nothing to do
    if type(some_list) != list:
        return ":"
    if len(some_list) == 0:
        return ":"
    #we check all the elements of the list
    for el in some_list:
        index += 1
        if type(el) == int:
    #for the first element we need to initialise the counters and remember the fisrt element in the sequence
            if current_el is None:
                current_el = el
                repeat_counter = 1
    #if elements repeats - we just count how many times
            elif current_el == el:
                repeat_counter += 1
    #if repeating series is finished we add an archived element into resulting string
            if current_el != el:
                if repeat_counter == 1: #single elements are not archived
                    result += str(current_el) +":"
                else:
                    result += f"{repeat_counter}|{current_el}" + ":" #repeating elements are archived
                repeat_counter = 1
                current_el = el

            if index == len(some_list): # if we reached the end of the list we add the last element to the result
                if repeat_counter == 1:
                    result += str(current_el)
                else:
                    result += f"{repeat_counter}|{current_el}"
        else:
            return ":" #non integer values will cancel the process of archivation
    return result

print(zip_list([0,1,2,3,4]))

#new
"""
author:Natalia

Подсчет сбалансированных строк
В этом задании нужно реализовать функцию count_balance(string: str) которая будет проверять сколько сбалансированных
подстрок включается в себя переданная строка.

Строки состоят из букв 'А' и 'Я' нужно определить сколько подстрок с одинаковым количеством этих букв находится
в переданной строке.

Пример 1:

Вход: s = "АЯААЯЯАЯАЯ"
Выход: 4
Объяснение: Можно выделить подстроки "АЯ", "ААЯЯ", "АЯ", "АЯ", каждая из этих подстрок содержит одинаковое
количество 'А' и 'Я'.
Пример 2:

Вход: s = "АЯЯЯЯААААЯ"
Выход: 3
Объяснение: здесь можно выделить подстроки "АЯ", "ЯЯЯААА", "АЯ", , каждая из этих подстрок содержит одинаковое
количество 'А' и 'Я'.
Пример 3:

Вход: s = "ААААЯЯЯЯА"
Выход: 1
Объяснение: Здесь можно выделить только подстроку "ААААЯЯЯЯ", для последней А нет буквы Я для баланса."""

def count_balance(string: str):
    current_char = ""
    series_count = [0, 0]
    series_index = 0
    last_char = 0
    result_strings = []
    if  type(string) != str:
        return 0
    string = string.upper()
    tmp_str = ""
    for char in string:
        if char in ("А", "Я"):
            tmp_str += char
    string = tmp_str

    for char in string:
        last_char += 1
        if current_char == "":
            current_char = char
            series_count[0] +=1
        else:
            if current_char == char:
                if series_index == 0:
                    series_count[0] += 1
                if series_index == 1:
                    if series_count[1] < series_count[0]:
                        series_count[1] += 1
                    else:
                        series_count[0] = min(series_count[0], series_count[1])
                        series_count[1] = series_count[0]
                        tmp_str = ""
                        tmp_char = ""
                        if char == "А":
                            tmp_char = "Я"
                        else:
                            tmp_char = "А"
                        for i in range (0, series_count[0]):
                            tmp_str = tmp_char + tmp_str + char
                        result_strings.append(tmp_str)
                        series_count = [1, 0]
                        series_index = 0
            else:
                if series_index == 0:
                    series_index = 1
                    series_count[1] +=1
                else:
                    series_count[0] = min(series_count[0], series_count[1])
                    series_count[1] = series_count[0]
                    tmp_str = ""
                    tmp_char = ""
                    if char == "А":
                        tmp_char = "Я"
                    else:
                        tmp_char = "А"
                    for i in range(0, series_count[0]):
                        tmp_str = tmp_char + tmp_str + char
                    result_strings.append(tmp_str)
                    series_index = 0
                    series_count = [1, 0]
                current_char = char
        if last_char == len(string) and series_count[1] > 0:
            series_count[0] = min(series_count[0], series_count[1])
            series_count[1] = series_count[0]
            tmp_str = ""
            tmp_char = ""
            if char == "А":
                tmp_char = "Я"
            else:
                tmp_char = "А"
            for i in range(0, series_count[0]):
                tmp_str = tmp_char + tmp_str + char
            result_strings.append(tmp_str)
    return len(result_strings)
print(count_balance("ААААЯЯЯЯА"))

#new
"""
author:Natalia

Эффективность рекламы
В этом задании нужно реализовать функцию, которая будет определять эффективность рекламной кампании.
На вход подается строка из трех чисел (прим: "0 100 70"). Первое это прибыль если реклама не будет запущена,
второе прибыль ожидаемую от запуска рекламы и третье это стоимость запуска рекламы. Нужно принять решение по
трем этим числам "Запускать" если дело прибыльное, "Не запускать" если это принесет убытки или "Без разницы"
если финансовый результат нулевой.

Пример 1

На вход: "0 100 70"
На выходе: "Запускать"
Объяснение: Тут выгода очевидна так как доход от рекламы с учетом расходов превышает доход если рекламу не запускать.
1) Данные будут передаваться только валидные в формате строки из трех чисел.

2) Возвращать нужно строго одну из трех строк: "Запускать", "Не запускать" или "Без разницы"""

def advertise_decision(adv: str):

    profit_no_ads = 0
    profit_with_ads = 0
    cost_ads = 0

    tmp = adv.split(" ")

    if len(tmp) >= 3:
        try:
            profit_no_ads, profit_with_ads, cost_ads = int(tmp[0]), int(tmp[1]), int(tmp[2])
        except ValueError:
            "Без разницы"
    ads_finance = profit_with_ads - cost_ads

    if ads_finance > profit_no_ads:
        return "Запускать"
    elif ads_finance < profit_no_ads:
        return "Не запускать"
    else:
        return "Без разницы"

print(advertise_decision("1 4 1 2 2 2 "))

 #new шифр цезаря

def c_crypt(msg: str, shift: int, alph: str) -> str:
    RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    EN = "abcdefghijklmnopqrstuvwxyz"

    if not (isinstance(msg, str) and isinstance(shift, int) and isinstance(alph, str)):
        return ""

    message = msg.replace(" ", "").lower()
    alph = alph.upper()

    if alph == "EN":
        alphabet = True
    elif alph == "RU":
        alphabet = False
    else:
        return ""

    if alphabet:
        p = len(EN)
    else:
        p = len(RU)

    if shift > 0:
        k = shift % p
    else:
        k = (-shift) % p * (-1)

    if alphabet:
        if k < 0:
            crypt_EN = EN[-k :] + EN[0:-k]
        elif k > 0:
            crypt_EN = EN[p-k:] + EN[0:p-k]
        else:
            crypt_EN = EN
    else:
        if k < 0:
            crypt_RU = RU[-k:] + RU[0:-k]
        elif k > 0:
            crypt_RU = RU[p - k:] + RU[0:p - k]
        else:
            crypt_RU = RU

    if alphabet:
        dict = message.maketrans(EN, crypt_EN)
    else:
        dict = message.maketrans(RU, crypt_RU)

    return message.translate(dict)

print(c_crypt("Как так?", 100, "ru"))

#new
"""
author:Natalia

Складываем числа, строки и массивы
В этом задании нужно реализовать функцию, которая будет уметь складывать между собой любую комбинацию
данных int, str и list.

- Если переданы типы которые можно сложить между собой, например числа, строки или списки, то вернуть
стандартный результат их сложения. Конкатенация строк или сложение чисел.

Если переданы строка и число:
- Если число первым аргументом, то вывести сумму этого числа и длины строки.

- Если строка передана первым аргументом, то выполнить конкатенацию строкового представления числа и строки.

Если один из аргументов list:
- Если list первым аргументом, то второй элемент нужно добавить в него.

- Если же list второй, то приводим его к строке и выполняем конкатенация как в примере.

Пример 1
sum_everything(1, 2) -> 3

Пример 2
sum_everything(1, "test") -> 5

Пример 3
sum_everything("1", 100) -> "1100"

Пример 4
sum_everything([], 100) -> [100]

Пример 5
sum_everything("1", []) -> "1[]"

Подсказка:

Как и любую другую проблему здесь можно обойтись условиями, но через перехват исключений решать проще.
Обратите внимание на сообщение ошибки."""

def sum_everything(a, b):

    if type(a) not in [str, int, list]:
        print("test")
        return None

    if type(a) == type(b):
        return a + b

    if isinstance(a, int) and isinstance(b, str):
        return a + len(b)

    if isinstance(a, str) and isinstance(b, int):
        return a + str(b)

    if isinstance(a, list):
        a.append(b)
        return a

    if isinstance(b, list):
        return str(a) + str(b)

print(sum_everything(3, []))

#new
"""
author:Natalia

Задаем классу поведение
В этом задании мы создадим свой класс с атрибутами и методами, которые будут эти атрибуты использовать.

Нужно будет создать несколько классов MobilePhone, AndroidPhone, iPhone.

Нужно самостоятельно определить какой класс сделать родительским, а какие будут наследниками.

У каждого мобильного устройства должна быть операционная система и поставщик этой системы (атрибуты _os и _os_vendor)
которые должны содержать значения либо Android/iOS и Google/Apple соответственно.

Каждое мобильное устройство должно уметь сообщать информацию о себе (иметь метод info()) который при вызове будет
возвращать сообщение "Mobile device based on {os} by {os_vendor}" где os и os_vendor это соответственно операционная
система и вендор телефона. Например, для  iPhone это будет "Mobile device based on iOS by Apple".

Каждое мобильное устройство должно уметь выполнять вызов (иметь метод call(phone_number)) по переданному номеру,
номер должен содержать только цифры и иметь длину строго 11. Если номер соответствует условиям, то нужно вернуть
сообщение "Calling to {phone_number} from {os} phone", иначе вернуть "Wrong phone number".

Важно учесть:

1) Общие методы должны передаваться только через наследование.

2) Все методы должны делать return, а не print"""

class MobilePhone:
    _os = None
    _os_vendor = None

    def __init__(self):
        pass

    def info(self):

        return "Mobile device based on {} by {}".format(self._os, self._os_vendor)

    def call(self, phone_number):
        try:
            number = int(phone_number)
        except ValueError:
            return "Wrong phone number"

        if  number in range(10000000000, 99999999999):
            return "Calling to {} from {} phone".format(number, self._os)
        else:
            return "Wrong phone number"

class AndroidPhone(MobilePhone):

    def __init__(self):
        self._os = "Android"
        self._os_vendor = "Google"

class iPhone(MobilePhone):

    def __init__(self):
        self._os = "iOS"
        self._os_vendor ="Apple"

#new
"""
author:Natalia
"""

def my_decorator(fun):
    def wrap():
        if fun()!= None:
            return "Функция вернула значение типа {}: {}".format(type(fun()), fun())
        else:
            return "Функция ничего не вернула"
    return wrap

@my_decorator
def some_function():
    return None

print(some_function())

#new
"""
author:Natalia
Создаём свой класс для вычитания строк
В этом задании нужно реализовать свой класс String экземпляры которого можно будет отнимать друг от друга .

Часть задания это поиск нужного волшебного метода, начать можно отсюда https://habr.com/ru/post/186608/,
с официальной документации или с гугла, самостоятельный поиск информации это один из навыков который нужно развивать.

Допустим, что при вычитании одного класса String от другого будут удалены все совпадающие буквы из первого
и вернётся результат в виде нового класса String.

Например:
s1 = String("aabbcdee")
s2 = String("abfdee")
res = s1 - s2 # "abc"
Что тут произошло? От первой строки последовательно отнимались первые вхождения символов второй строки. Т.е.
убрали буквы "a", "b", "d", "ee", так как нет вхождения буквы f, то с ней ничего не делали. Букв "a" и "b" в
первой строке было по 2, а во второй строке по одной, то и осталось в результате по одной букве, а букв "e"
было по 2 в обоих строках и потому в итоговом результате не осталось ни одной. Буква "c" осталась так как не
присутствует во второй строке.

Важные моменты:

1. В качестве результата вы должны возвращаться класс String а не строку.

2. Вам нужно реализовать дополнительно метод для сравнения экземпляров (этот метод тоже нужно найти самостоятельно)
класса String на равенство. Т.е. String("abc") == String("abc") должно возвращать True, а String("cba") == String("abc")
должен вернуть False."""

class String:

    def __init__(self, string):
        self.val = string

    def __repr__(self):
        return 'String("{}")'.format(self.val)

    def __sub__(self, other):
        str1 = self.val
        str2 = other.val
        res = ""
        chars = []
        for char in str1:
            if char not in chars:
                n_char = max(str1.count(char) - str2.count(char), 0)
                chars.append(char)
                for i in range(0, n_char):
                    res += char
        return String(res)

    def __eq__(self, other):
        if self.val == other.val:
            return True
        else:
            return False

s1 = String("aabbcdee")
s2 = String("abfdee")
s3 = String("aabbcdee")
res = s1 - s2
print(res)
print(s1 == s2)
print(s1 == s3)

#new
"""
author:Natalia

счетчик экземпляров
"""


class HowMuch:
    # Пишите вашу реализацию здесь
    created_amount = 0
    deleted_amount = 0
    exist_amount = 0

    def __init__(self):
        self.up_counter()
        self.set_exist_amount()

    def __del__(self):
        self.up_del_counter()
        self.set_exist_amount()

    @classmethod
    def up_counter(cls):
        cls.created_amount +=1

    @classmethod
    def up_del_counter(cls):
        cls.deleted_amount += 1

    @classmethod
    def set_exist_amount(cls):
        cls.exist_amount = cls.created_amount - cls.deleted_amount
    @classmethod
    def describe(cls):
        return "HowMuch instances: deleted - {}, created - {}, exist - {}".format(cls.deleted_amount, cls.created_amount, cls.exist_amount)


print(HowMuch.describe())

obj1 = HowMuch()
print(HowMuch.describe())
del  obj1
print(HowMuch.describe())
obj1 = HowMuch()
obj2 = HowMuch()
print(HowMuch.describe())

#new
"""
author:Natalia

Создаем класс наполненный странной магией
В этом задании вам нужно будет реализовать поведение для класса с помощью волшебных методов.

У класса будет очень странное поведение:

1) Методом bool() он всегда должен приводиться к False

2) Инициализируется любым элементом, который потом приводится к строке

3)  Методом float() должен возвращать случайное значение от 0 до длины переданного элемента в строковом прдставлении
(учтите что возвращать нужно только float значение)

4) При делении любого int или float числа на экземпляр класса, деление должно выполняться на длину строки которой он
проинициализиирован.

Пример 1:
example = Solution("test")
print(float(example)) # -> 3.0 (т.к. находится в диапазоне от 0 до 4)
print(bool(example)) # -> False
print(100 / example) # -> 25.0
На занятии мы не разбирали все необходимые для выполнения методы, но вы обладаете пониманием как они должны работать и
что нужно гуглить ;)"""

from __future__ import division
import random

class Solution:
    value = None
    # Напишите вашу реализацию здесь
    # Так же для этого задания вам потребуется модуль random ;)
    def __init__(self, string):
        self.value = str(string)

    def __bool__(element):
        return False

    def __str__(self):
        return self.value

    def __float__(element):
        return random.uniform(0, len(str(element)))

    """def __truediv__(self, other):
        return float(len(self.value) / other)"""

    def __rtruediv__(self, other):
        return float(other / len(self.value))

example = Solution("test")
example1 = Solution("t")
print(bool(example))
print(float(example))
print(100 / example)

#new
"""
author:Natalia

Пишем свой банк ч.1 (Account)
В этой задаче нужно реализовать класс Account у которого должно быть упрощённое поведение реального банковского счёта.

0. Все сообщения брать из примера работы.

1. Счёт должен инициализироваться только именем владельца.

2. Каждому счёту автоматически присваивается 6ти значный идентификатор "aid" (account id).

3. Идентификатор увеличивается при создании нового счёта.

4. У счёта должны быть защищенные для прямого изменения атрибуты: balance, aid. При попытке их изменить не должно быть
исключений или ошибок, они просто сохраняют своё значение.

5. У счёта должны быть реализованы методы deposit и withdraw, которые пополняют и снимают деньги со счёта. Баланс счёта
не должен допускать уход в минус, если средств недостаточно нужно вернуть сообщение как в примере ниже и баланс не
менять. При успешном пополнении или снятии средств нужно вернуть сообщение с текущим балансом (формат смотри в примере).
Методы не должны работать с закрытым счётом (см. пункт 6).

6. У счёта должен быть метод close который закрывает счёт, после закрытия на счёте должны быть недоступны операции
пополнения и снятия средств, так же счёт нельзя закрыть дважды, вместо этого нужно вернуть сообщение как в примере ниже.

Пример работы (значения у всех методов возвращаемые, принты в классе не использовать):

account1 = Account("Mike Tyson")
account2 = Account("Cameron Diaz")

print(account1.aid) # 0000001
print(account2.aid) # 0000002

# Закрытие счёта
print(account2.close()) # Account '000002' closed
print(account2.deposit(1000)) # Can't deposit deactivated account
print(account2.withdraw(1000)) # Can't withdraw from deactivated account
print(account2.close()) # Account already closed

# Операции по счёту
print(account1.deposit(1000)) # Balance: 1000
print(account1.balance) # 1000
print(account1.close()) # Can't close not empty account
print(account1.withdraw(999)) # Balance: 1
print(account1.close()) # Can't close not empty account
print(account1.withdraw(10)) # Not enough balance
print(account1.withdraw(1)) # Balance: 0
print(account1.close()) # Account '000001' closed

# Защита данных от изменения
account3 = Account("Trest Tester")
print(account3.aid) # 000003
account3.owner = "Evil Devil"
print(account3.owner) # "Trest Tester"
account3.balance = 999999
print(account3.balance) # 0
account3.aid = "001000"
print(account3.aid) # 000003"""

class Account():
	owner = None
	aid = None
	balance = 0
	COUNTER = 0
	internal_call = None
	closed = None

	def __init__(self, name):
		self.internal_call = True
		self.owner = name
		self.up_counter()
		self.aid = str(self.COUNTER).zfill(6)
		self.balance = 0
		self.closed = False
		self.internal_call = False

	def __setattr__(self, name, value):
		if (self.internal_call):
			self.__dict__[name] = value
		else:
			if name in ("aid", "balance", "owner"):
				pass
			else:
				self.__dict__[name] = value

	@classmethod
	def up_counter(cls):
		cls.COUNTER += 1

	def deposit(self, amount):
		if not self.closed:
			if isinstance(amount, int) or isinstance(amount, float):
				self.internal_call = True
				self.balance += amount
				self.internal_call = False
				return "Balance: {}".format(self.balance)
			else:
				return "Wrong amount"
		else:
			return "Can't deposit deactivated account"

	def withdraw(self, amount):
		if not self.closed:
			if isinstance(amount, int) or isinstance(amount, float):
				self.internal_call = True
				if self.balance >= amount:
					self.internal_call = True
					self.balance -= amount
					self.internal_call = False
					return "Balance: {}".format(self.balance)
				else:
					return "Not enough balance"
			else:
				return "Wrong amount"
		else:
			return "Can't withdraw from deactivated account"

	def close(self):
		if not self.closed:
			if self.balance != 0:
				return "Can't close not empty account"
			self.closed = True
			return "Account '{}' closed".format(self.aid)
		else:
			return "Account already closed"


account1 = Account("Mike Tyson")
account2 = Account("Cameron Diaz")

print(account1.aid) # 0000001
print(account2.aid + "\n\n") # 0000002

print(account2.close()) # Account '000002' closed
print(account2.deposit(1000)) # Can't deposit deactivated account
print(account2.withdraw(1000)) # Can't withdraw from deactivated account
print(account2.close() + "\n\n") # Account already closed

print(account1.deposit(1000)) # Balance: 1000
print(account1.balance) # 1000
print(account1.close()) # Can't close not empty account
print(account1.withdraw(999)) # Balance: 1
print(account1.close()) # Can't close not empty account
print(account1.withdraw(10)) # Not enough balance
print(account1.withdraw(1)) # Balance: 0
print(account1.close() + "\n\n") # Account '000001' closed

account3 = Account("Trest Tester")
print(account3.aid) # 000003
account3.owner = "Evil Devil"
print(account3.owner) # "Trest Tester"
account3.balance = 999999
print(account3.balance) # 0
account3.aid = "001000"
print(account3.aid) # 000003

"""
author:Natalia

Считаем слова в текстовом файле

В этом задании нужно реализовать функцию count_words_in_file(filename: str, word: str) которая принимает в качестве
аргументов имя файла и слово, после чего возвращает количество раз которые это слово встречается в файле. В упражнение
включен файл text.txt в качестве примера, для отладки можно использовать его."""
import os

def count_words_in_file(filename: str, word: str):
    with open(filename) as file:
        counter = file.read().count(word)
    return counter

print(count_words_in_file("text.txt", "рjhgjg"))

#new
"""
author:Natalia
Подсчитываем среднюю стоимость продажи
В этом заднии вам дан файл с двумя колонками [SALE_ID, SALE_PRICE] где первое это ID продажи, а вторая это сумма.
В данном небольшом заднии нужно просто посчитать какова средняя стоимость продажи на предоставленных данных и вывести
подсчитанное значение на экран с помощью print (код вывода на экран и открытия файла уже написан, его менять не нужно)"""

import csv

avg_sale_price = 0
row_count = 0
with open('input.csv') as csvfile:
    # Пишите код работы c данными здесь.
    reader = csv.DictReader(csvfile)
    for line in reader:
        row_count +=1
        avg_sale_price += float(line.get('SALE_PRICE'))

avg_sale_price /= row_count
# В конце задания нужно вывести среднюю стоимость продажи, округлив до 2х знаков после запятой.
# Так как ответ можно подобрать и просто вывести его на экран, при проверке производятся математические операции над
# данными, так что просто написать число после падения теста не выйдет и оно всегда будет разным, но вы же не будете
# так делатть ;)
#
print(round(avg_sale_price, 2))

#NEW
# записная книжка
# { Python: Быстрый старт, Тема: Базы данных }

import sqlite3


def get_connection():
    con = sqlite3.connect("notebook.sqlite3")
    con.execute("""
        CREATE TABLE IF NOT EXISTS data
        (name TEXT, phone TEXT, age INTEGER)
    """)
    return con


def insert_data(connection, name, phone, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)", (name, phone, age))
    connection.commit()
    print("Данные успешно добавлены")


def show_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    for el in cursor.fetchall():
        print(*el)


def delete_by_name(connection, name):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE name = ?", (name,))
    connection.commit()
    print("Данные успешно удалены")


if __name__ == "__main__":
    print("Добро пожаловать в записную книжку!")

    action = None

    while action != 'exit':
        con = get_connection()
        action = input("Выберите действие [add, read, delete]\n")

        if action == 'add':
            try:
                name, phone, age = input("Введите данные (name phone age): ").split(" ")
            except ValueError:
                print("Неверно введены данные")
            else:
                insert_data(con, name, phone, age)
        elif action == 'read':
            show_data(con)
        elif action == 'delete':
            name_to_delete = input("Введите имя контакта на удаление: ")
            delete_by_name(con, name_to_delete)
        else:
            con.close()
            print("Пока, пока")
            exit(0)

#new

"""
author:Natalia""
Напишем свой генератор
В этом задании нужно написать свой собственный генератор, который будет на вызов метода next возвращать заданное
количество следующих чисел возведенных в переданную степень.

Проще понять это на примере:

gen = my_generator(12, 2, 5) # Нужно возвращать 5 числе начиная с 12 возведнных во 2 степень

next(gen)  -> 144 (квадрат 12)
next(gen) -> 169 (квадрат 13)
next(gen) -> 196 ...
next(gen) -> 225
next(gen) -> 256
next(gen) -> на этом вызове выбрасывается исключение StopIteration"""

def my_generator(value: int, power: int, amount: int):
    # Реализуйте ваш генератор здесь
    for i in range(0, amount):
        res = (value + i) ** power
        yield res

gen = my_generator(12, 2, 5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#new
import requests
from http import HTTPStatus

response = requests.get("https://jsonplaceholder.typicode.com/comments", params={"postId": "1"})
response = requests.post(f"https://jsonplaceholder.typicode.com/posts", json={"user": "admin", "password": "qwerty123" })
print(HTTPStatus.OK)
print(HTTPStatus(response.status_code).description)
print(response.text)
print(response.json()[3])

for post in response.json():
    print(post["name"])
#new
