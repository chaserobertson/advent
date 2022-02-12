import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('18', 'input.txt')

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

# given a parenth-less expression, evaluate additions first
def adv_evaluate(exp):
    if '+' in exp:
        plus_ind = exp.find('+')
        left = plus_ind-2
        while left-1 >= 0 and exp[left-1] != ' ':
            left -= 1
        right = plus_ind+2
        while right+1 < len(exp) and exp[right+1] != ' ':
            right += 1
        plus_result = str(simple_evaluate(exp[left:right+1]))
        pre_plus = exp[:left]
        post_plus = exp[right+1:]
        return adv_evaluate(pre_plus + plus_result + post_plus)
    else:
        return simple_evaluate(exp)

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
        sub_exp_result = str(parenth_evaluate(sub_exp))
        new_exp = exp[:parenth_inds[0]] + sub_exp_result + exp[parenth_inds[1]+1:]
        return parenth_evaluate(new_exp)
    else:
        return adv_evaluate(exp)


print('part 2')
results = []
for line in lines:
    val = parenth_evaluate(line.strip())
    results.append(val)
print(results)
print(sum(results))
