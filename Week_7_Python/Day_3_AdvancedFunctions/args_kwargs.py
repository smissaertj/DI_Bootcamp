def dummy(*args):
    print(args)
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(args[4])
    print(args[5])


dummy(1, 2, 3, 4, 5, 'hello')

numbers = [10, 20, 5]
print(sum(numbers))


def out_sum(*args):
    sum_of_numbers = 0
    for num in args:
        sum_of_numbers += num

    return sum_of_numbers

result = out_sum(1, 2, 3, 4, 5)
print(result)


# ===========================================

def check_arguments_keyworded_arguments (required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

check_arguments_keyworded_arguments("required argument")
check_arguments_keyworded_arguments("required argument", 1, 2, 'hey')
check_arguments_keyworded_arguments("required argument", 1, 2, 'hey', name="Sarah", age=24)


# =====================================

# *args ==> Tuple
# **kwargs ==> Dictionary

def print_arguments(*args, **kwargs):
    print(f'The input args (tuple) are: {args}')
    print(f'The input kwargs (dict) are: {kwargs}')

print_arguments(5, 3, age=10, name='joeri')