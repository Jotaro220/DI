from Generate_big_number import generate_prime, find_primes_in_range
from key_exchange import diffie_hellman_key_exchange
from primitive_roots import find_primitive_roots


def main_menu():
    prime = None

    while True:
        print("\nЛабораторная работа №5 - Меню:")
        print("1. Сгенерировать простое число заданной битности")
        print("2. Найти все простые числа в диапазоне")
        print("3. Найти первообразные корни для заданного числа")
        print("4. Моделировать обмен ключами Диффи-Хеллмана")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            bits = int(input("Введите количество бит: "))
            k = int(input("Введите количество проверок Рабина-Миллера: "))
            prime, iterations, time_taken = generate_prime(bits, k)
            print(f"Сгенерировано простое число: {prime}")
            print(f"Потребовалось итераций: {iterations}")
            print(f"Затраченное время: {time_taken:.4f} секунд")

        elif choice == "2":
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            primes, time_taken = find_primes_in_range(start, end)
            print(f"Найдено простых чисел: {len(primes)}")
            print(f"Затраченное время: {time_taken:.4f} секунд")
            if len(primes) <= 100:
                print("Простые числа:", primes)
            else:
                print("Первые 100 простых чисел:", primes[:100])

        elif choice == "3":
            n = int(input("Введите число n: "))
            roots, time_taken = find_primitive_roots(n)
            print(f"Найдено первообразных корней: {len(roots)}")
            print(f"Затраченное время: {time_taken:.4f} секунд")
            print("Первые 100 первообразных корней:", roots)

        elif choice == "4":
            diffie_hellman_key_exchange(prime)

        elif choice == "5":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()