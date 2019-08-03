def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message


if __name__ == '__main__':

    log_hi = logger('Welcome!')
    log_hi()