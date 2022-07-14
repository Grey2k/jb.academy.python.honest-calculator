# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'

YES = 'y'
NO = 'n'

OPERATIONS = [
    ADD,
    SUB,
    MUL,
    DIV
]

memory = 0


def calculate(x, y, operation):
    if operation not in OPERATIONS:
        raise ValueError(msg_2)

    if operation == ADD:
        return x + y
    if operation == SUB:
        return x - y
    if operation == MUL:
        return x * y
    if operation == DIV:
        if y == 0:
            raise ValueError(msg_3)

        return x / y


def is_int(item: str) -> bool:
    return item.lstrip('-+').isdigit()


def is_float(item: str) -> bool:
    try:
        float(item)
        return True
    except ValueError:
        return False


def check_number(x):
    if is_int(x):
        x = int(x)
    elif is_float(x):
        x = float(x)
    elif x == 'M':
        x = memory
    else:
        raise ValueError(msg_1)

    return x


def is_one_digit(num: float):
    if -10 < num < 10:
        if num.is_integer():
            return True

    return False


def check(x, y, operator) -> None:
    msg = ""

    x = float(x)
    y = float(y)

    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6

    if (x == 1 or y == 1) and operator == MUL:
        msg += msg_7

    if (x == 0 or y == 0) and operator in [MUL, SUB, ADD]:
        msg += msg_8

    if msg != "":
        print(msg_9 + msg)


def main():
    x, operation, y = input().strip().split()

    x = check_number(x)
    y = check_number(y)

    check(x, y, operation)

    return float(calculate(x, y, operation))


def need_memorize(res):
    print(msg_4)
    msg_index = 10

    msgs = {
        10: msg_10,
        11: msg_11,
        12: msg_12
    }

    memorize = input().strip()
    if memorize == YES and is_one_digit(res):
        while True:
            print(msgs.get(msg_index))
            answer = input().strip()
            if answer == NO:
                break
            if answer == YES:
                if msg_index < 12:
                    msg_index += 1
                    continue
                return True

        return False

    return True


while True:
    try:
        print(msg_0)
        result = main()
        print(result)

        if need_memorize(result):
            memory = result

        print(msg_5)
        need_continue = input().strip()

        if need_continue == YES:
            continue

        break
    except ValueError as err:
        print(err)
