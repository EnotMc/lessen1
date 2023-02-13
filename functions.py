#Функции

#задание 1

def get_summ(one,two,delimiter='&'):
    func=f'{one}{delimiter}{two}'
    return func
variable = get_summ('Learn','python')
print(variable.upper()) 

#Задание 2

def format_price(price):
    price = int(price)
    func=f'Цена: {price} руб.'
    return func
variable = format_price(56.24) 
print(variable)   