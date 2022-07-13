def result(x):
    str_list = [str(x)*i for i in range(1, x+2)]
    print(str_list)
    print('+'.join(str_list))
    return sum(map(int, str_list))

print(result(3))