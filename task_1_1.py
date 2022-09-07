# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day = int(input('Enter a week day number: '))
if 5 < week_day <=7:
    print(f'{week_day} -> yes')
else:
    print(f'{week_day} -> no')