def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


if __name__ == '__main__':

    hello_func = outer_func('Hello!')
    hi_func = outer_func('Hi')

    hello_func()
    hi_func()