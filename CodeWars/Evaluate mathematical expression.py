'''
Instructions
Given a mathematical expression as a string you must return the result as a number.

Numbers
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

Operators
You need to support the following mathematical operators:

Multiplication *
Division / (as floating point division)
Addition +
Subtraction -
Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

Parentheses
You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace
There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers 
and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10

And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid

Validation
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.

Restricted APIs
NOTE: eval and exec are disallowed in your solution.
'''


def calc(expression):
    # Received strings
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    noNumbers = {'+', '-', '*', '/', '(', ')', '.'}
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
        }
    conta = []
    # 1 - removed whitespaces
    removeSpace = expression.replace(' ','')
    # 2 - Creat a list os Strings
    print(removeSpace)
    print('passo 1')
    conta = [a if a in noNumbers else int(a) for a in removeSpace]
    print(conta)
    # 3 - Transform list os string in a list with float
    conta2 = []
    decimal = ''
    for b in range(len(conta)):
        print('2 passo')
        if type(conta[b]) == int:
            print('2 passo - numero int')
            decimal += str(conta[b])
        elif conta[b] == '.':
            print('2 passo - ponto')
            decimal += conta[b]
        else:
            if decimal != '':
                print('2 passo - decimal')
                conta2.append(float(decimal))
                decimal = ''
            conta2.append(conta[b])
    if decimal != '':
        print('2 passo - final')
        conta2.append(float(decimal))
    # 5 - Replace all "-" sign
    if '-' in conta2:
        while '-' in conta2:
            print('3 passo')
            for indice, valor in reversed(list(enumerate(conta2))):
                if valor == '-':
                    print('3 passo - negativo')
                    i = indice
                    if conta2[i+1] == '(':
                        print('3 passo - multiplica * -1')
                        conta2.insert(i,'*')
                        conta2.insert(i,-1)
                        conta2.pop(i+2)
                        if type(conta2[i-1]) == float and i != 0 :
                            print('3 passo - insserir o +')
                            conta2.insert(i,'+')
                            break
                        break
                    conta2[i+1] = conta2[i+1] * -1
                    if conta2[i-1] == ')':
                        print('3 passo - negativo com ()')
                        conta2[i] = '+'
                        break
                    if type(conta2[i-1]) == float and i != 0 :
                        print('3 passo - negativo +')
                        conta2[i] = '+'
                        break
                    else:
                        print('3 passso - fim')
                        conta2.pop(i)
                        break
    # 6 - Resolve all () and nested (())
    if '(' in conta2:
        while '(' in conta2:
            print('4 passo')
    # 6.1 Solve the * -1
            parFim = conta2.index(')')
            conta3 = conta2[:parFim]
            parIni = len(conta3) - list(reversed(conta3)).index('(') - 1
            conta3 = conta3[parIni + 1:]
            while len(conta3) >= 3:
                print('4 passo - começo')
                # 6.2 - Resolve * and / first
                while '*' in conta3 or "/" in conta3:
                    print('4 passo - tirar os -1')
                    for indice, valor in enumerate(conta3):
                        if valor == -1 and conta2[indice + 2] != '(':
                            i = indice
                            conta4 = [operadores[conta3[i+1]](conta3[i],conta3[i+2])]
                            conta3 = conta3[:i] + conta4 + conta3[i+3:]
                            break
                    for indice, valor in enumerate(conta3):
                        print('4 passo - tirar os * e /')
                        if valor == '*' or valor == '/':
                            i = indice
                            numIni = i - 1
                            conta4 = [operadores[conta3[i]](conta3[i-1],conta3[i+1])]
                            conta3 = conta3[:numIni] + conta4 + conta3[i+2:]
                            break
                        elif type(float):
                            continue
                # 6.3 - Resolve + later
                while '+' in conta3:
                    print('4 passo - segundo passo')
                    for indice, valor in enumerate(conta3):
                        print('4 passo - tirar os +')
                        if valor == '+' or valor == '-':
                            i = indice
                            numIni = i - 1
                            conta4 = [operadores[conta3[i]](conta3[i-1],conta3[i+1])]
                            conta3 = conta3[:numIni] + conta4 + conta3[i+2:]
                            break
                        elif type(float):
                            continue
                break
            if len(conta3) < 3:
                print('4 passo - final? ou inútil? AAAAAAAAAAAAAAAAA')
                conta2 = conta2[:parIni] + conta3 + conta2[parFim + 1:]
    # 7 - Resolve the rest of equation
    while len(conta2) > 2:
        print('5 passo')
        # 7.1 - Solve * and / first
        while '*' in conta2 or "/" in conta2:
            print('5 passo - inicio')
            for indice, valor in enumerate(conta2):
                print('5 passo - tirar os * e /')
                if valor == '*' or valor == '/':
                    i = indice
                    numIni = i - 1
                    conta3 = [operadores[conta2[i]](conta2[i-1],conta2[i+1])]
                    conta2 = conta2[:numIni] + conta3 + conta2[i+2:]
                    break
                elif type(float):
                    continue
        # 7.2 - Solve the + after
        while '+' in conta2:
            print('5 passo - segunda parte')
            for indice, valor in enumerate(conta2):
                print('5 passo - tirar os +')
                if type(valor) == str:
                    i = indice
                    numIni = i - 1
                    conta3 = [operadores[conta2[i]](conta2[i-1],conta2[i+1])]
                    conta2 = conta2[:numIni] + conta3 + conta2[i+2:]
                    break
                elif indice == 0:
                    continue
    if len(conta2) == 2:
        print('6 - passo opcional antibug')
        conta2 = [conta2[0] + conta2[1]]
    return conta2[0]


print(calc('-(-58) + (94 * 5 / (56)) - (-14 * -(((-(48 + -61)))) * 75)'))

# (19 + 70 / -(59)) V
# -(26) / (19 + 70 / -(59)) * (76 + -(((-(-24 - 16)))) + 38) V
# (1 + 2) + (3 + 4) V
# 1 + (2 + (3 + 4)) V
# 1 + 2 + 3 + 4  V
# 1 + (2 + 3 + 4) V
# (((10))) V
# 1 + 2 * 3 = 7 V
# 2 + 2 + 3 * 3 + 4 * 2 + 5 * 2 V
# 1 + 3 * 5 / (2 * 8 + 5 -(3 + 4 + 5 * 2)) V
# 1 - -5 V
# 4--5 + 4 * (1--1) V
# 6 + -(4) V
# -(-1) V
# 3-(-1) V
# 6 + -( -4) V
# -7 * -(6 / 3) V
# 7 * -(6 + 3)V
