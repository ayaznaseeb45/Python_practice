def is_valid(text):
    stack = []

    for ch in text:

        # Opening bracket
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)

        # Closing bracket
        else:

            if len(stack) == 0:
                return False

            last = stack.pop()
            

            if ch == ")" and last != "(":
                return False

            if ch == "]" and last != "[":
                return False

            if ch == "}" and last != "{":
                return False

    return len(stack) == 0


print(is_valid("()"))        
print(is_valid("()[]{}"))    
print(is_valid("(]"))        
print(is_valid("([{}])"))   
print(is_valid("([)]"))      
print(is_valid("((("))      