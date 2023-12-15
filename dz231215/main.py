def f1(a, b, c, d):
    return [0] + a, [0] + b, [0] + c, [1] + d
def f2(a, b, c, d):
    a0 = a.pop(0)
    b0 = b.pop(0)
    c.pop(0)
    d.pop(0)
    if c[0]:
        if d[0]:
            b[0] *= a0 + b0
        else:
            b[0] /= a0 + b0
    else:
        a[0] += b[0]
        if d[0]:
            b[0] = a0 + b0
        else:
            b[0] = -(a0 + b0)
    return a, b, c, d
def f3(a, b, c, d):
    c[0] = 0
    d[0] = 1
    return a, b, c, d
def f4(a, b, c, d):
    c[0] = 0
    d[0] = 0
    return a, b, c, d
def f5(a, b, c, d):
    c[0] = 1
    d[0] = 1
    return a, b, c, d
def f6(a, b, c, d):
    c[0] = 1
    d[0] = 0
    return a, b, c, d
def f7(a, b, c, d, v):
    if c[0]:
        if d[0]:
            b[0] *= v
        else:
            b[0] /= v
    else:
        if d[0]:
            a[0] += b[0]
            b[0] = v
        else:
            a[0] += b[0]
            b[0] = -v
    return a, b, c, d


fsm = {
    'initial': 'q0',
    'transitions': {
        'q0': {'(': ('q0', f1), ')': ('q0', f2), '+': ('q0', f3), '-': ('q0', f4), '*': ('q0', f5), '/': ('q0', f6), 'd': ('q0', f7)},
        'q1': {},
    }
}

def fsm_do(fsm, input_str):
    d = None
    new_input_str = []
    for i in input_str:
        if i.isdigit():
            if d is None:
                d = 0
            d *= 10
            d += int(i)
        elif i != " ":
            if d is not None:
                new_input_str.append(d)
            d = None
            new_input_str.append(i)
    if d is not None:
        new_input_str.append(d)
    a = [0]
    b = [0]
    c = [0]
    d = [1]
    current_state = fsm['initial']

    for symbol in new_input_str:
        if symbol in fsm['transitions'][current_state]:
            a, b, c, d = fsm['transitions'][current_state][symbol][1](a, b, c, d)
            current_state = fsm['transitions'][current_state][symbol][0]
        else:
            v = int(symbol)
            a, b, c, d = fsm['transitions'][current_state]['d'][1](a, b, c, d, v)
            current_state = fsm['transitions'][current_state]['d'][0]
    return a[0] + b[0]

input_str = "(2+4 - 3)*3 - 1"
result = fsm_do(fsm, input_str)
print(f"Input string '{input_str}' result: {result}")