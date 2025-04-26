import random

from Generate_big_number import generate_prime
from primitive_roots import find_primitive_roots


def diffie_hellman_key_exchange(prime):
    print("Генерация общих параметров:")
    if prime == None:
        n_bits = int(input("Введите количество бит для простого числа n: "))
        n, _, _ = generate_prime(n_bits)
        print(f"Сгенерировано простое число n: {n}")
    else:
        n = prime

    roots, _ = find_primitive_roots(n, 1)
    if not roots:
        print("Не удалось найти первообразный корень для данного n")
        return
    g = roots[0]
    print(f"Найден первообразный корень g: {g}")

    # Генерация секретных ключей
    XA = random.randint(2, n - 2)
    XB = random.randint(2, n - 2)

    # Вычисление открытых ключей
    YA = pow(g, XA, n)
    YB = pow(g, XB, n)

    # Обмен открытыми ключами и вычисление общего секрета
    KA = pow(YB, XA, n)
    KB = pow(YA, XB, n)

    print("\nРезультаты обмена ключами:")
    print(f"Секретный ключ A (XA): {XA}")
    print(f"Секретный ключ B (XB): {XB}")
    print(f"Открытый ключ A (YA): {YA}")
    print(f"Открытый ключ B (YB): {YB}")
    print(f"Общий секретный ключ (KA): {KA}")
    print(f"Общий секретный ключ (KB): {KB}")
    print(f"Проверка совпадения ключей: {'OK' if KA == KB else 'ERROR'}")\


#11185973915640637787