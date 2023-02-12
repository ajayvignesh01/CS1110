# Ajay Chandrasekaran (HPD2DZ)

current_value = int(0)
recent_operation = str('')
recent_argument = int()
series = str('0')


def get_value():
    return current_value


def clear(c=0):
    global current_value, recent_operation, recent_argument, series
    current_value = int(c)
    recent_operation = str('')
    recent_argument = int()
    series = str(c)
    return current_value


def step(operator, x):
    global current_value, recent_operation, recent_argument, series
    if operator == '+':
        current_value += x
    elif operator == '-':
        current_value -= x
    elif operator == '*':
        current_value *= x
    elif operator == '//':
        current_value //= x
    recent_operation = operator
    recent_argument = x
    series = '(' + series + ')' + recent_operation + str(recent_argument)
    return current_value


def repeat():
    global current_value, recent_operation, recent_argument
    if recent_operation == '':
        return current_value
    else:
        current_value = step(recent_operation, recent_argument)
        return current_value


def get_expr():
    global series
    return series