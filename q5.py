def str_f(str):
    if len(str) == 1:
        return str[0]
    elif str[0] != str[1]:
        return str[0] + str_f(str[1:])
    else:
        return str_f(str[1:])



