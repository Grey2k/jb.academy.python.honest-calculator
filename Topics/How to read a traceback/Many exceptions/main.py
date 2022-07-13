import math


def find_sqrt(number):
    try:
        print(math.sqrt(int(number)))
    except TypeError:
        print('Please pass a number like "5" or 5')
    except ValueError:
        print('Please pass a number like "5" or 5')
