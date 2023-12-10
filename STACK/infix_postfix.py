# application of stack - infix to postfix
def infix_to_postfix(exp):
    postfix = []
    operator = []
    priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    for ch in exp:
        if ch == "(":
            operator.append(ch)
        elif ch == ")":
            while operator[-1] != "(":
                ele = operator.pop()
                postfix.append(ele)
            operator.pop()
        elif ch == "^" or ch == "*" or ch == "/" or ch == "+" or ch == "-":
            if len(operator) > 0:
                while priority[operator[-1]] >= priority[ch]:
                    ele = operator.pop()
                    postfix.append(ele)
                    if len(operator) == 0:
                        break
            operator.append(ch)
        else:
            postfix.append(ch)

    while len(operator) != 0:
        ele = operator.pop()
        postfix.append(ele)
    return postfix


if __name__ == "__main__":
    exp = input("Enter infix expression: ")
    postfix = infix_to_postfix(exp)

    print("Infix expression = ", exp)
    print("Postfix expression = ", end=" ")
    for ele in postfix:
        print(ele, end="")
