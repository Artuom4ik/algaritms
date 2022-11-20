import random


def bin_search(left, right):
    current = random.randint(left, right)
    count = 0
    while True:    
        is_right = input(f'Ваше число {current}? (да, >, <) ')
        count += 1
        if is_right == '>':
            left = current + 1
        elif is_right == '<':
            right = current - 1
        else:
            print(f'Ура!!! Я угадал. За {count} попыток') 
            break   
        current = round((right + left) / 2)


if __name__ == '__main__':
    left = int(input('Миннимвльное число '))
    right = int(input('максимальное число '))
    print(f'Загадай число от {left} до {right}. Я отгадаю его меньще чем за 10 попыток')
    bin_search(left, right)
