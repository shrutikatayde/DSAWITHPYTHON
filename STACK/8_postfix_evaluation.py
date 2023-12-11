from infix_postfix import infix_to_postfix

exp = input("Enter infix expression: ")
postfix = infix_to_postfix(exp)
print("Postfix Expression for evaluation: ", postfix)

operator = ["+", "-", "*", "/", "^"]
operand = []

for ele in postfix:
    if ele not in operator:
        operand.append(ele)
    else:
        n1 = eval(operand.pop())
        n2 = eval(operand.pop())
        if ele == "+":
            ans = n2 + n1
        elif ele == "-":
            ans = n2 - n1
        elif ele == "*":
            ans = n2 * n1
        elif ele == "/":
            ans = n2 / n1
        elif ele == "^":
            ans = n2 ** n1
        operand.append(str(ans))

print("Postfix Evaluation: ", operand[0])
