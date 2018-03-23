# coding = utf-8

import hashlib


def jm(d, s=''):

    temp = hashlib.md5((para(d) + 'key=' + s).encode('utf-8')).hexdigest().upper()
    # print (para(d) + 'key=' + s)
    return temp


def para(d):

    temp = list(d.keys())
    temp.sort()
    s = ''
    for key in temp:
        if type(d[key]) == float:
            d[key] = int(d[key])
        if str(d[key]) != '':
            s += str(key) + '=' + str(d[key]) + '&'

    return s


if __name__ == "__main__":

    print (jm({'a': '中国', 'c': 1.0, 'd': 'str'}, 'test'))
