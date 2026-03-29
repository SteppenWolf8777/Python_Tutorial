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
