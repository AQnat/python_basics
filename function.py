
def training_func(name, greeting):
    return f'{name}, {greeting}'
    #return '{}, {}'.format(name, greeting) --> the same resault

if __name__ == '__main__':

    print(training_func('Adam', 'try to do something better!').upper())