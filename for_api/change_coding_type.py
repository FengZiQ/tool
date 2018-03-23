# coding = utf-8
import json


def handling(d):

    for key in d.keys():

        if type(d[key]) == float:
            d[key] = int(d[key])
        elif type(d[key]) == str and '#dict' not in d[key] and str(d[key]).endswith('}'):
                d[key] = json.loads(d[key])
        elif type(d[key]) == str and '#list' in d[key]:
                d[key] = str(d[key]).split('#list')
                if '' in d[key]:
                    d[key].remove('')
        elif type(d[key]) == str and '#dict' in d[key]:
                d[key] = str(d[key]).split('#dict')
                if '' in d[key]:
                    d[key].remove('')