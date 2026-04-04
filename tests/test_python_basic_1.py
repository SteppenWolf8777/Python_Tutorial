def test_greeting_and_mood():
    """Тест 1: приветствие пользователя и реакция на настроение"""
    print("Как Вас зовут?")
    username = input()
    print(f"Здравствуйте, {username}!")
    print("Как дела?")
    mood = input()
    if mood == "хорошо":
        print("Я за Вас рада!")
    elif mood == "плохо":
        print("Всё наладится!")



def test_compare_two_speeds():
    """Тест 2: сравнение скоростей Пети и Васи"""
    p_speed = float(input())
    v_speed = float(input())
    if p_speed > v_speed:
        print("Петя")
    else:
        print("Вася")



def test_compare_three_speeds():
    """Тест 3: сравнение скоростей Пети, Васи и Толи"""
    p_speed = float(input())
    v_speed = float(input())
    t_speed = float(input())
    if p_speed > v_speed and p_speed > t_speed:
        print("Петя")
    elif t_speed > v_speed and t_speed > p_speed:
        print("Толя")
    else:
        print("Вася")



def test_leap_year():
    """Тест 4: проверка, является ли год високосным"""
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("YES")
    else:
        print("NO")



def test_palindrome_number():
    """Тест 5: проверка, является ли четырёхзначное число палиндромом"""
    number = int(input())
    a = number // 1000  # первая цифра
    b = (number // 100) % 10  # вторая цифра
    c = (number // 10) % 10  # третья цифра
    d = number % 10  # четвёртая цифра
    if a == d and b == c:
        print("YES")
    else:
        print("NO")



def test_find_lexicographically_smallest_name():
    """Тест 6: нахождение лексикографически наименьшего имени"""
    name1 = input()
    name2 = input()
    name3 = input()

    if name1 <= name2 and name1 <= name3:
        print(name1)
    elif name2 <= name1 and name2 <= name3:
        print(name2)
    else:
        print(name3)



def test_password_processing():
    """Тест 7: обработка пароля — формирование числа из сумм цифр"""
    password = int(input())

    # Извлекаем цифры числа
    hundreds = password // 100  # цифра сотен
    tens = (password // 10) % 10  # цифра десятков
    units = password % 10  # цифра единиц

    # Находим суммы
    sum_last_two = tens + units  # сумма десятков и единиц (двух младших цифр)
    sum_first_two = hundreds + tens  # сумма сотен и десятков (двух старших цифр)

    # Записываем суммы в порядке невозрастания (от большей к меньшей)
    if sum_first_two >= sum_last_two:
        result = int(str(sum_first_two) + str(sum_last_two))
    else:
        result = int(str(sum_last_two) + str(sum_first_two))

    print(result)


def test_triangle_existence():
    """Тест 8: проверка существования треугольника"""
    a = float(input())
    b = float(input())
    c = float(input())

    # Проверяем условие существования треугольника:
    # сумма любых двух сторон должна быть строго больше третьей стороны
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("YES")
    else:
        print("NO")


def test_filter_fruits():
    """Тест 9: фильтрация фруктов, содержащих букву 'a'"""
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
        if "a" in x:
            newlist.append(x)

    print(newlist)


# Пример вызова всех тестов (можно раскомментировать нужные)
if __name__ == "__main__":
    test_greeting_and_mood()
    test_compare_two_speeds()
    test_compare_three_speeds()
    test_leap_year()
    test_palindrome_number()
    test_find_lexicographically_smallest_name()
    test_password_processing()
    test_triangle_existence()
    test_filter_fruits()