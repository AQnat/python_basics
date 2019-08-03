import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments "{}"'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x*y

def sub(x, y):
    return x+y

if __name__ == '__main__':

    add_logger = logger(add)
    sub_logger = logger(sub)

    add_logger(2, 5)
    add_logger(3, 7)

    sub_logger(4, 8)
    sub_logger(6, 12)