#!/usr/bin/python3

rules = {}
messages = []
with open('19/test2.txt', 'r') as f:
    for line in f.readlines():
        # if its a rule line
        if ':' in line:
            ruletxt = line.split(':')
            rulenum = int(ruletxt[0].strip())
            # if its a terminal rule
            if '"' in line:
                ruleval = ruletxt[1].split('"')[1]
                rules.setdefault(rulenum, ruleval)
            # else its a recursive rule
            else:
                rulevals = ruletxt[1].split('|')
                for i in range(len(rulevals)):
                    rulevals[i] = [int(x) for x in rulevals[i].strip().split()]
                rules.setdefault(rulenum, rulevals)
        # if its a message line
        elif line != '\n':
            messages.append(line.strip())

def printrules():
    for key, val in rules.items():
        print(key, ':', val)

def possibilities(rules, rule):
    if type(rule) == str:
        return [rule]
    elif type(rule) == int:
        return possibilities(rules, rules[rule])
    else:
        poss = '('
        for i in range(len(rule)):
            option = rule[i]
            op_str = '' if i == 0 else '|'
            for op in option:
                for p in possibilities(rules, rules[op]):
                    op_str += p
            poss += op_str
        
        return poss+')'

def checkterminal(rule, message):
    #print('terminal check', rule, message)
    if message == None or len(message) < 1:
        return None
    elif len(message) == 1 and message[0] == rule:
        return ''
    elif message[0] == rule:
        return message[1:]
    else:
        return None

def checkoption(rules, option, message):
    #print('option check', option, message)
    result = message
    for req in option:
        result = checkmatch(rules, rules[req], result)
    return result

def checkmatch(rules, rule, message):
    #print('match check', rule, message)
    # base case: terminal rule
    if type(rule) == str:
        return checkterminal(rule, message)
    # should be a list: recursive rule
    else:
        for option in rule:
            postop = checkoption(rules, option, message)
            if postop != None:
                return postop
        return None

#printrules()
#print(messages)
# was only 42
#rules[8] = [[42], [42, 8]]
# was only [42, 31]
#rules[11] = [[42, 31], [42, 11, 31]]
print(possibilities(rules, rules[31]))

matches = 0
for m in messages:
    c = checkmatch(rules, rules[0], m)
    #print(c)
    if c == '':
        matches += 1
print(matches)