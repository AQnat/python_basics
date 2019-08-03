vege = {'ogórek' : 'zielony', 'marchewka' : 'pomarańczowy', 'pomidor' : 'czerwony', 'cebula' : 'biały'}
vege_str = ', '.join(vege)
vege_values = ', '.join(vege.values())
#vege_items =

if __name__ == '__main__':

    print(' ')

    print(vege)
    print(vege['marchewka'])
    print(vege.keys())
    print(vege.values())
    print(vege.items())
    print('  ' + vege_str.upper())
    print('  ' + vege_values.lower())
    #print(vege_items())

    print(' ')

    for key in vege:
        print(key)
    print(' ')

    for key, values in vege.items():
        print(values)
    print(' ')

    for values in vege.items():
        print(values)
    print(' ')

    for keys, values in vege.items():
        print(keys, values)
    print(' ')

    for keys, values in vege.items():
        print(f"{keys} - {values}")