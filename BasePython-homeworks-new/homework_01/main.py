"""
Домашнее задание №1
Функции и структуры данных
"""

def is_prime(number):
    if len([devs for devs in range(2, int(number**0.5)+1) if (number % devs)==0]) == 0:
        return True
    else:
        return False
    
def power_numbers(*num):
    print([int(square)**2 for square in num])
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
def even_numbers(num):
    if num%2==0:
        return num
    # return [even for even in num if int(even)%2==0]

def odd_numbers(num):
    if num%2!=0:
        return num
    # return [odd for odd in num if int(odd)%2!=0]

def prime_numbers(num):
    if is_prime(num)==True:
        return num

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num, filter_numbers):
    if filter_numbers == "odd":
        print(list(filter(odd_numbers, num)))
    if filter_numbers == "even":
        print(list(filter(even_numbers, num)))
    if filter_numbers == "prime":
        print(list(filter(prime_numbers, num)))
    """
    функция, которая на вход принимает список из целых чисел,~
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

power_numbers(1, 2, 5, 7)
filter_numbers([1, 2, 3, 4, 8, 9, 10, 11, 20, 21], ODD)
filter_numbers([2, 3, 4, 5, 13, 17, 19, 20], EVEN)
filter_numbers([2, 3, 4, 5, 6, 7, 9, 11, 13, 18, 19, 20, 27], PRIME)