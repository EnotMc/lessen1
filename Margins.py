#Отступы

import random

def is_more_than_five(number):
    if number > 5:
        print('Больше 5')
    else:
        print('Меньше 5')

rand_num = random.randint(1, 10)
is_more_than_five(rand_num)