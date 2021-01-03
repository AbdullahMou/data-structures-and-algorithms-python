def multi_bracket_validation(strings):

    brackets = []
    valid = { '(':')', '[':']', '{':'}' }

    for x in strings:
        if (x == '(' or x == '{' or x == '['):
            brackets.append(x)
        elif x in valid.values():
            if len(brackets) == 0:
                return False
            val = brackets.pop()
            if x != valid[val]:
                return False

    if len(brackets) != 0:
        return False
    
    return True

if __name__ == "__main__":
    print(multi_bracket_validation('(){}[[]]'))    
    print(multi_bracket_validation('{}{Code}[Fellows](())'))    
    print(multi_bracket_validation('[({}]'))    
    print(multi_bracket_validation('{(})'))    