def  html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


if __name__ == '__main__':

    print_h1 = html_tag('h1')
    print_h1('Text headline')
    print_h1('Another headline')