import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('18', 'smol_input.txt')

with open(in_file) as input:
    lines = input.readlines()

OPERATORS = ['+', '-', '*']
OPERATOR_SET = set(OPERATORS)


def execute(arg1, op, arg2):
    if op == OPERATORS[0]:
        return arg1 + arg2
    elif op == OPERATORS[1]:
        return arg1 - arg2
    elif op == OPERATORS[2]:
        return arg1 * arg2


# given a parenth-less expression, evaluate left to right
def simple_evaluate(exp):
    args = exp.split(' ')
    arg1 = None
    op = None
    for arg in args:
        if arg1 == None:
            arg1 = int(arg)
            continue
        elif arg in OPERATOR_SET:
            op = arg
            continue
        else:
            arg2 = int(arg)
            arg1 = execute(arg1, op, arg2)
            op = None
    return arg1


def get_parenth_inds(exp):
    inds = [exp.index('(')]
    open_stack = 0
    for i in range(inds[0], len(exp)):
        char = exp[i]
        if char == '(':
            open_stack += 1
        elif char == ')':
            if open_stack == 1:
                inds.append(i)
                return inds
            else:
                open_stack -= 1
    return None


def parenth_evaluate(exp):
    if '(' in exp:
        parenth_inds = get_parenth_inds(exp)
        if parenth_inds == None:
            print('bad bad')
            return -1
        sub_exp = exp[parenth_inds[0] + 1:parenth_inds[1]]
        sub_exp_result = parenth_evaluate(sub_exp)
        mid = str(sub_exp_result)
        new_exp = exp[:parenth_inds[0]] + mid + exp[parenth_inds[1]+1:]
        return parenth_evaluate(new_exp)
    else:
        return simple_evaluate(exp)


print('part 1')
results = []
for line in lines:
    val = parenth_evaluate(line)
    results.append(val)
print(results)
print(sum(results))
