# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'

OPERATIONS = [
    ADD,
    SUB,
    MUL,
    DIV
]


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
    else:
        raise ValueError(msg_1)

    return x


def main():
    x, operation, y = input().strip().split()

    x = check_number(x)
    y = check_number(y)

    print(float(calculate(x, y, operation)))


while True:
    try:
        print(msg_0)
        main()
        break
    except ValueError as err:
        print(err)
