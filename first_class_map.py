
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


if __name__ == '__main__':

    squares = my_map(cube, [1, 2, 3, 4, 5])
    print(squares)