# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 100
string1 = 'total'
print(f'{string1} = {a} печенек')

user_name = input('Введите ваше имя: ')
user_age = input('Введите ваш возраст: ')
print(f'Данные пользователя №{a}:\nИмя: {user_name.upper()}; Возраст: {user_age}')

# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_seconds = int(input('Введите время в секундах: '))
seconds = user_seconds % 60
minutes = user_seconds % 3600 // 60
hours = user_seconds // 3600
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_digit = input('Enter a number 0-9: ')

while user_digit < '0':
    user_digit = input('Your number must be grater than 0: ')

print(f'{int(user_digit) + int(user_digit * 2) + int(user_digit * 3)}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = input('Enter a number of some digits: ')
i = 1
max_num = user_num[0]

while i < len(user_num):
    if max_num < user_num[i]:
        max_num = user_num[i]
        if max_num == 9:
            break
    i += 1
print(f'The greatest digit in number {user_num} is {max_num}')

# def num_max(num):
#     if num < 10:
#         return num
#     else:
#         m = num_max(num // 10)
#         return m if m > num % 10 else num % 10
#
#
# print(f"The largest number is: {num_max(int(input('Enter the number: ')))}")

"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
income = float(input('Введите выручку фирмы: '))
costs = float(input('Введите издержки фирмы: '))
result = income - costs
if result > 0:
    print(f'Финансовый результат: Прибыль! {result}')
    print(f'Рентабельность выручки: {result / income:.3f}')
    employee_num = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {result / employee_num:.3f}')
elif result == 0:
    print('Прибыль равна нулю!')
else:
    print(f'Финансовый результат: Убыток! {-result}')

"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

a = float(input('Введите количество км в первый день: '))
b = float(input('Введите желаемое количество км для расчета дня: '))

progress = a
day = 1
while progress < b:
    progress += progress * 0.1
    day += 1

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')


# def km(res_min, res_max, days):
#     if res_min > res_max:
#         return days
#     else:
#         return km(res_min * 1.1, res_max, days + 1)
#
#
# print(km(int(input("Enter km at first day: ")), int(input("Enter desired km: ")), 1))
