# -*- coding: utf-8 -*-
# 2018.04.25

import base64


def encrypt(s=''):
    encrypt_str = base64.b64encode(s.encode(encoding='utf-8'))
    print(encrypt_str)

    s_s = base64.b64decode(encrypt_str.decode())

    print(s_s)

if __name__ == "__main__":
    encrypt('Inspiry2o180')