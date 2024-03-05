from stack import Stack as stack

operatorList = ['+', '-', '*', '/', '^']

def initializer(inputPhrase):
    isChangeApplied = True
    phrase = inputPhrase

    while isChangeApplied:

        isChangeApplied = False


        i = 0
        while i < len(phrase) - 1:
            if phrase[i] == '-' and phrase[i + 1] == '-':
                phrase = phrase[:i] + "+" + phrase[i + 2:]
                isChangeApplied = True


            elif phrase[i] == '-' and phrase[i + 1] == '+':
                phrase = phrase[:i] + '-' + phrase[i + 2:]
                isChangeApplied = True


            elif phrase[i] == '+' and phrase[i + 1] == '+':
                phrase = phrase[:i] + '+' + phrase[i + 2:]
                isChangeApplied = True
            i += 1

    return phrase

def is_valid_input(input_string):
    validCharacters = "1234567890.*-+/^()"
    flag = True
    for i in range(len(input_string)):
        flag = flag and input_string[i] in validCharacters
        if not flag: break

    return flag

def nodeMaker(expression):
    nodeList = []
    number = ''
    last_char = None
    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        elif char in operatorList:
            if number:
                nodeList.append(number)
                number = ''

            if char == '-' and (last_char in operatorList or last_char is None or last_char == '('):
                number = char
            elif char == '+' and last_char in operatorList:

                pass
            else:
                nodeList.append(char)
        elif char in '()':
            if number:
                nodeList.append(number)
                number = ''
            nodeList.append(char)
        last_char = char
    if number:
        nodeList.append(number)
    return nodeList



def calculator(expression):
    expressionNodedList = nodeMaker(expression)
    i = 0
    while i < len(expressionNodedList):
        if expressionNodedList[i] == '^':
            result = pow(float(expressionNodedList[i-1]), float(expressionNodedList[i+1]))
            expressionNodedList[i-1:i+2] = [str(result)]
            continue
        i += 1

    i = 0
    while i < len(expressionNodedList):
        if expressionNodedList[i] == '*':
            result = float(expressionNodedList[i-1]) * float(expressionNodedList[i+1])
            expressionNodedList[i-1:i+2] = [str(result)]
            continue
        elif expressionNodedList[i] == '/':
            if float(expressionNodedList[i + 1]) == 0:
                print("Division by zero is not allowed.")
                exit(0)
            result = float(expressionNodedList[i-1]) / float(expressionNodedList[i+1])
            expressionNodedList[i-1:i+2] = [str(result)]
            continue
        i += 1

    i = 0
    while i < len(expressionNodedList):
        if expressionNodedList[i] == '+':
            result = float(expressionNodedList[i-1]) + float(expressionNodedList[i+1])
            expressionNodedList[i-1:i+2] = [str(result)]
            continue
        elif expressionNodedList[i] == '-':
            result = float(expressionNodedList[i-1]) - float(expressionNodedList[i+1])
            expressionNodedList[i-1:i+2] = [str(result)]
            continue
        i += 1

    return expressionNodedList[0] if expressionNodedList else '0'




def evaluate_expression(phrase):
    open_parentheses_stack = stack()
    for i, char in enumerate(phrase):
        if char == '(':
            open_parentheses_stack.push(i)
        elif char == ')':
            start = open_parentheses_stack.pop()
            sub_expression = phrase[start + 1:i]

            value = calculator(sub_expression)

            phrase = phrase[:start] + str(value) + phrase[i + 1:]
            return evaluate_expression(phrase)  # recursive
    return calculator(phrase)


input_phrase = input("Enter your mathematical expression (you can only use +, -, *, /, ^ and ()): ")
if is_valid_input(input_phrase):
    input_phrase = initializer(input_phrase)
    print(evaluate_expression(input_phrase))
else: print("Invalid input entered")

