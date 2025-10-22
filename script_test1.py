from collections import Counter

while True:
    s = input('Введите последовательность цифр: ')
    if s.isdigit():
        break
    print('Только цифры!!!\n')

counter = Counter(s)

for number, count in counter.items():
    print(f"Число {number}: повторется {count} раз")

while True:
    n = input(f'Вывести n первых элементов последовательности "{s}": ')
    if not n.isdigit():
        print('Только цифры!!!\n')
        continue
    n = int(n)
    if n > len(s):
        print(f'Введите число не больше {len(s)}\n')
    print(s[:n])
    break