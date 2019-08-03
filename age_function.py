"""
Describing feature based on people's age
"""

nick = input('What\'s your name? ').capitalize()

while True:
    try:
        age = int(input('How old are you? '))
        break
    except ValueError:
        print('Put the correct number.'.upper())


def user_feature(nick, age):

    if age <= 0:
        return f'You cannot back to the yesterdays, unfortunately.'
    elif 0 < age <= 12:
        return f'{nick}, you are a child.'
    elif 12 <= age < 18:
        return f'{nick}, you are a teenager.'
    elif age == 18:
        return f'{nick}, you are an adult from now - go and vote!.'
    elif 18 < age < 24:
        return f'{nick}, probably you are a student, maybe would be.'
    elif age % 10 == 0 and not age == 10 and not age == 20:
        return f'{nick}, real life is just beginning.'
    elif 24 <= age < 65:
        return f'{nick}, you have the best age to work hard.'
    elif 65 <= age <= 99:
        return f'{nick}, you have to retired.'
    elif age >= 100:
        return f'{nick}, that\'s impossible! :-O'
    else:
        return f'Is that true?'


if __name__ == '__main__':

    print(user_feature(nick, age))