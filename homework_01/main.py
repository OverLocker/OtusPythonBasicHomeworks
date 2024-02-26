"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [i ** 2 for i in args]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n: int) -> bool:
    is_n_prime = True
    if n not in (0,1):
        for d in range(2, n//2+1):
            if n % d == 0:
                is_n_prime = False
                break
    else:
        is_n_prime = False
    return is_n_prime



def filter_numbers(numbers: list, arg: str) -> list:
    if arg == EVEN:
        result = [int(n) for n in numbers if n % 2 == 0]
    if arg == ODD:
        result = [int(n) for n in numbers if n % 2 != 0]
    if  arg == PRIME:
        result = list(filter(is_prime, numbers))
    return result



    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
