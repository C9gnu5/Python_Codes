def evaluate_expression(expression):
    def solve_expression(operators, operand):
        operator = operators.pop()
        right = operand.pop()
        left = operand.pop()

        if operator == "+":
            operand.append(left + right)
        elif operator == "-":
            operand.append(left - right)
        elif operator == "*":
            operand.append(left * right)
        elif operator == "/":
            if right == 0:
                raise ValueError("Zero Division Error")
            operand.append(left / right)

    operand = []
    operators = []

    for _ in expression:
        if _.isdigit():
            operand.append(int(_))
            if len(operand) > (len(operators)+1):
                right = operand.pop()
                left = operand.pop()
                operand.append(int(str(left)+str(right)))
        elif _ in {"+", "-", "*", "/", "("}:
            operators.append(_)
        elif _ == ")":
            while operators and operators[-1] != "(":
                solve_expression(operators, operand)
            operators.pop()

            if len(operand) == 2 or len(operand) > 2:
                right = operand.pop()
                left = operand.pop()
                operand.append(right * left)
        else:
            raise ValueError("A value in expression is invalid")
        
    while operators:
        if '(' in operators and ')' not in operators:
            raise ValueError("Found no closing parenthesis")
        solve_expression(operators, operand)

    if len(operand) != 1 or operators:
        raise ValueError("Invalid expression, something went wrong!")

    return operand[0]

try:
    expression = input("Enter the arithmetic expression: ")
    print("Valid Arithmetic Expression, the result is", evaluate_expression(expression))
except ValueError as e:
    print("Error:", e)
    