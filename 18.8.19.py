sum = 0
tickets = int(input("Введите количество билетов:\n"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:\n"))
    if age < 18:
        sum += 0
    elif age >= 18 and age <= 25:
        sum += 990
    elif age > 25:
        sum += 1390
if sum == 0:
    print("Проходите на конференцию!")
else:
    print("Стоимость Ваших билетов:", "%.2f" % sum, "руб.")

if tickets > 3:
    discount = sum / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате:", "%.2f" % (sum -discount), "руб.")