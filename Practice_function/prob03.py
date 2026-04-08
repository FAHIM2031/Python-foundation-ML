def power(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] ** args[1]
    else:
        raise ValueError("Invalid number of arguments")

print(power(2,5))
print(power(5))