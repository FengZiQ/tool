# -*- coding: utf-8 -*-

import requests
import json


def barcodeString():

    url = 'https://uat.access.mynt.xyz/xapi/2.1/mac/gcash/barcode/generate'
    body = {
        "gcashWalletName": "09178263348",
        "type": "01"
    }
    headers = {
        'X-UDID': '4b4686bfb358e0fc6022108347ad1232',
        'X-Gateway-Auth': 'YW5kcm9pZDphbmRyb2lk',
        'Content-Type': 'application/json',
        'Authorization': 'Token gYpewc_-gsQz2qHpF7E4',
        'x-auth': 'APIAuth 4b4686bfb358e0fc6022108347ad1232:BPI9YYjdc15saCdiDa42LSYVfpWxSNfxOYTEiFpANTA='
    }
    content = requests.post(url, data=None, json=body, headers=headers)

    result = json.loads(content.text)

    print(result['data']['barcodeString'])


if __name__ == "__main__":

    for i in range(10):
        barcodeString()