# application of stack - infix to postfix
def infix_to_prefix(exp):
    prefix = []
    operator = []
    priority = {")": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    for ch in exp[::-1]:
        if ch == ")":
            operator.append(ch)
        elif ch == "(":
            while operator[-1] != ")":
                ele = operator.pop()
                prefix.append(ele)
            operator.pop()
        elif ch == "^" or ch == "*" or ch == "/" or ch == "+" or ch == "-":
            if len(operator) > 0:
                while priority[operator[-1]] > priority[ch]:
                    ele = operator.pop()
                    prefix.append(ele)
                    if len(operator) == 0:
                        break
            operator.append(ch)
        else:
            prefix.append(ch)

    while len(operator) != 0:
        ele = operator.pop()
        prefix.append(ele)
    return prefix


if __name__ == "__main__":
    exp = input("Enter infix expression: ")
    prefix = infix_to_prefix(exp)

    print("Infix expression = ", exp)
    print("Prefix expression = ", end=" ")
    for ele in prefix[::-1]:
        print(ele, end="")
