import time


def gcd(a, b):
    """Наибольший общий делитель (НОД) двух чисел."""
    while b:
        a, b = b, a % b
    return a


def is_primitive_root(g, p, phi):
    """Проверяет, является ли g первообразным корнем по модулю p."""
    if gcd(g, p) != 1:
        return False

    factors = []
    n = phi
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.append(n)

    for factor in factors:
        if pow(g, phi // factor, p) == 1:
            return False
    return True


def find_primitive_roots(p, num_roots=100):
    """Находит первые num_roots первообразных корней по модулю p."""
    phi = p - 1  # Функция Эйлера для простого числа p
    roots = []
    g = 2
    start_time = time.time()

    while len(roots) < num_roots and g < p:
        if is_primitive_root(g, p, phi):
            roots.append(g)
        g += 1

    end_time = time.time()
    total_time = end_time - start_time

    return roots, total_time





# Пример использования:
p = 11185973915640637787  # Замените на нужное простое число


num_roots_to_find = 100
primitive_roots, total_time = find_primitive_roots(p, num_roots_to_find)

print(f"Первые {len(primitive_roots)} первообразных корней по модулю {p}:")
print(primitive_roots)
print(f"Суммарное время поиска: {total_time:.4f} секунд")