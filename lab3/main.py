def rvp(infix):
    stack = []
    postfix = ""
    operators = ['+', '-', '*', '/', '(', ')']
    priority = {'+':1, '-':1, '*':2, '/':2}

    for c in infix:
        if c not in operators:
            postfix += c
        elif c=='(':
            stack.append(c)
        elif c==')':
            while len(stack)>0 and stack[-1]!='(':
                postfix += stack.pop()
            stack.pop()
        else:
            while len(stack)>0 and stack[-1]!='(' and priority[c]<=priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(c)

    while len(stack)>0:
        postfix += stack.pop()

    return postfix



def main():
    print(rvp("((2+7)/3+(8−3)*4)/2")) # 2 7 + 3 / 8 3 − 4 * + 2 /

if __name__ == "__main__":
    main()

