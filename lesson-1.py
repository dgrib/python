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
if seconds < 10:
    seconds = f'0{seconds}'
minutes = user_seconds % 3600 // 60
if minutes < 10:
    minutes = f'0{minutes}'
hours = user_seconds // 3600
if hours < 10:
    hours = f'0{hours}'
print(f'{hours}:{minutes}:{seconds}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_digit = input('Введите число 0-9: ')
n = int(user_digit)
nn = int(user_digit*2)
nnn = int(user_digit*3)
print(n+nn+nnn)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = input('Введите число из нескольких цифр: ')
i = 1
max_num = user_num[0]

while i < len(user_num):
    if max_num < user_num[i]:
        max_num = user_num[i]
    i += 1
print(f'Самая большая цифра в числе: {max_num}')

"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
income = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if income > costs:
    print('Финансовый результат: Прибыль!')
    profit = income / costs # рентабельность выручки
    print(f'Рентабельность выручки: {profit}')
    employee_num = int(input('Введите количество сотрудников фирмы: '))
    employee_profit = profit / employee_num # рентабельность фирмы на одного сотрудника
    print(f'Прибыль фирмы в расчете на одного сотрудника: {employee_profit}')
else:
    print('Финансовый результат: Убыток!')

"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""

a = int(input('Введите количество км в первый день: '))
b = int(input('Введите желаемое количество км для расчета дня: '))

progress = a
day = 1
while progress < b:
    progress += progress*0.1
    day +=1

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
