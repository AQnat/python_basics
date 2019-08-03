names = ('Adam', 'Bob', 'Celine', 'Diana', 'Estera')
names_str = ', '.join(names)


if __name__ == '__main__':
    print(' ')

    print(names)
    print('  ' + names_str.lower())
    print(names_str.upper())

    print(' ')

    for name in (names):
        print(name)

    print(' ')

    for index, name in enumerate(names, start=1):
        print(index, name.upper())

