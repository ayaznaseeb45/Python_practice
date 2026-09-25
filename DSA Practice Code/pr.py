def brackets_check(text):
    stack = []

    for ch in text:
        # opening brackets 
        if ch == "(" or ch =="[" or ch =="{":
            stack.append(ch)

        # closing brackets 
        else:
            if len(stack) == 0:
                return False

            last = stack.pop()

            if ch == ")" and last !="(":
                False

            if ch == "]" and last !="]":
                False

            if ch == "}" and last !="{":
                False

    return len(stack) == 0     

print(brackets_check("()"))