import random


def bin_search(left, right):
    global bin_count
    current = random.randint(left, right)
    bin_count = 0
    while True:    
        bin_count += 1
        if number > current:
            left = current + 1
        elif number < current:
            right = current - 1
        else:
            print(f'Ура!!! Я угадал. За {bin_count} попыток') 
            break   
        current = round((right + left) / 2)


def lin_search(left):
    global lin_count
    current = left
    lin_count = 0
    while True:
        lin_count += 1
        if number != current:
            current += 1
        else:
            print(f'Ура!!! Я отгадал твоё число за {lin_count} попыток')
            break


if __name__ == '__main__':
    lin_score = 0
    bin_score = 0
    for i in range(1, 6):
        left = int(input('Миннимвльное число '))
        right = int(input('максимальное число '))
        number = int(input('Введите число для поиска '))
        print(f'Загадай число от {left} до {right}. Я отгадаю его меньще чем за 10 попыток')
        bin_search(left, right)
        lin_search(left)
        print(f'Результат соревнования: линейный поиск - {lin_count}, бинарный поиск- {bin_count}')
        if lin_count > bin_count:
            bin_score += 1
        elif lin_count < bin_count:
            lin_score += 1
        else:
            bin_count += 1
            lin_count += 1
            print('Ничья')
    if lin_score > bin_score:
        print('Победил линейный поиск')
    elif lin_score < bin_score:
        print('Победил бинарный поиск')
    else:
        print('Ничья')