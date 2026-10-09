# 07.10.2026

def do_nothing():
    pass

def make_a_sound():
    print('quack')

make_a_sound()  #call


def echo(anything):
    return anything + ' ' + anything

print(echo('WORD'))

def calculate_discount(price, discount_percent=10):
    return price * discount_percent / 100

print(calculate_discount(155, 12))

final_price = calculate_discount(100, 25)
print(f'Final price: ${final_price}')  # discount_percent will be 25 since last assinged params = 100 and 25

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range(1, 5)

for x in ranger:
    print(x)


def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("START")

        result = func(*args, **kwargs)

        print("END")

        return result

    return wrapper

@start_end_decorator
def good(name):
    return ['Harry', 'Ron', 'Hermione']

print(good('Harry'))  # START, END, ['Harry', 'Ron', 'Hermione']

