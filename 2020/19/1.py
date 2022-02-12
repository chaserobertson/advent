#!/usr/bin/python3

rules = {}
messages = []
with open('19/input.txt', 'r') as f:
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

matches = 0
for m in messages:
    c = checkmatch(rules, rules[0], m)
    #print(c)
    if c == '':
        matches += 1
print(matches)