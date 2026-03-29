print("Как Вас зовут?")
username = input()
print(f"Здравствуйте, {username}!")
print("Как дела?")
mood = input()
if mood == "хорошо":
    print("Я за Вас рада!")
elif mood == "плохо":
    print("Всё наладится!")


p_speed = float(input())
v_speed = float(input())
if p_speed > v_speed:
    print('Петя')
else:
    print('Вася')


p_speed = float(input())
v_speed = float(input())
t_speed = float(input())
if p_speed > v_speed and p_speed > t_speed:
    print('Петя')
elif t_speed > v_speed and t_speed > p_speed:
    print('Толя')
else:
    print('Вася')


year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")


number = int(input())
a = number // 1000           # первая цифра
b = (number // 100) % 10     # вторая цифра
c = (number // 10) % 10      # третья цифра
d = number % 10              # четвертая цифра
if a == d and b == c:
    print("YES")
else:
    print("NO")


name1 = input()
name2 = input()
name3 = input()

if name1 <= name2 and name1 <= name3:
    print(name1)
elif name2 <= name1 and name2 <= name3:
    print(name2)
else:
    print(name3)