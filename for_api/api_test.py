# coding = utf-8
# 2018.03.05

from remote import Server
from to_log import tolog
from sign import *
from change_coding_type import handling
import json
import xlrd
import time
import random

Pass = "'result': 'p'\n"
Fail = "'result': 'f'\n"

server = Server()


class APITest(object):

    def __init__(self):
        self.flag = False
        self.method = ''
        self.serverIp = ''
        self.service = ''
        self.cases_file = ''
        self.optional = []
        self.must = []

    # For test of method 'post/put/delete' and confirm response
    def settings_test(self, cases_sheet, must_response_sheet, hold_time=0):
        # Open cases file
        data = xlrd.open_workbook(self.cases_file)
        table1 = data.sheet_by_name(cases_sheet)
        table2 = data.sheet_by_name(must_response_sheet)

        # test all parameters
        for j in range(2, table1.nrows):

            # Building body parameters
            settings = dict((table1.cell(1, i).value, table1.cell(j, i).value) for i in range(1, table1.ncols))
            expected = dict((table2.cell(1, i).value, table2.cell(j, i).value) for i in range(1, table2.ncols))

            # Conversion data or data type
            handling(settings)

            if 'pp_trade_no' in settings.keys() and self.service == 'api/scannedCode':
                num = random.randint(1, 1000)
                settings['pp_trade_no'] = str(num*100) + str(settings['pp_trade_no'])

            if 'sign' in settings.keys():
                t = settings['sign']
                settings.pop('sign')
                settings['sign'] = jm(settings, str(t))

            handling(expected)

            # Expected result
            tolog('Body: ' + json.dumps(settings, ensure_ascii=False, indent=2).replace('\n', ''))
            tolog('Expected Response: ' + json.dumps(expected, ensure_ascii=False, indent=2).replace('\n', ''))

            # Sending request
            result = server.webapi(self.method, self.serverIp, self.service, settings)

            temp = json.loads(result["text"])

            handling(temp)

            if str(result['response']) != '<Response [200]>':
                self.flag = True
                tolog('Fail: HTTP status code is ' + str(result['response']))
                tolog('Error Message: ' + json.dumps(temp, ensure_ascii=False, indent=2).replace('\n', '') + '\n')
            else:
                for key in expected.keys():
                    try:
                        if str(expected[key]) != '' and str(expected[key]) not in str(temp[key]):
                            self.flag = True
                            tolog('Fail: Expected ' + str(key) + ' is ' + str(expected[key]) + '; Actuality is ' + str(temp[key]))
                    except KeyError:
                        self.flag = True
                        tolog('Fail: Missing parameter ' + str(key))
                else:
                    tolog('HTTP status code is ' + str(result['response']))
                    tolog('Actual response: ' + json.dumps(temp, ensure_ascii=False, indent=2).replace('\n', ''))
                    tolog('-*- The case is executed! -*-\n')

            time.sleep(hold_time)

        # test optional parameters
        optional_settings = dict((table1.cell(1, i).value, table1.cell(2, i).value) for i in range(1, table1.ncols))
        response_must = dict((table2.cell(1, i).value, table2.cell(2, i).value) for i in range(1, table2.ncols))

        handling(optional_settings)
        handling(response_must)

        if len(self.optional) != 0:
            for p in self.optional:
                p_value = optional_settings.pop(p)
                pay_key = ''
                # Conversion data or data type
                if 'pp_trade_no' in optional_settings.keys() and self.service == 'api/scannedCode':
                    num = random.randint(1, 100)
                    optional_settings['pp_trade_no'] = str(num) + str(optional_settings['pp_trade_no'])
                if 'sign' in optional_settings.keys():
                    pay_key = optional_settings['sign']
                    optional_settings.pop('sign')
                    optional_settings['sign'] = jm(optional_settings, str(pay_key))

                # Expected result
                tolog('Remove optional parameter: ' + str(p))
                tolog('Body: ' + json.dumps(optional_settings, ensure_ascii=False, indent=2).replace('\n', ''))
                tolog('Expected Response: ' + json.dumps(response_must, ensure_ascii=False, indent=2).replace('\n', ''))

                # Sending request
                result = server.webapi(self.method, self.serverIp, self.service, optional_settings)

                temp = json.loads(result["text"])
                handling(temp)

                if str(result['response']) != '<Response [200]>':
                    self.flag = True
                    tolog('Fail: HTTP status code is ' + str(result['response']))
                    tolog('Error Message: ' + json.dumps(temp, ensure_ascii=False, indent=2).replace('\n', ''))
                    tolog('-*- The case is executed! -*-\n')
                else:
                    for key in response_must.keys():
                        try:
                            if str(response_must[key]) != '' and str(response_must[key]) not in str(temp[key]):
                                self.flag = True
                                tolog('Fail: Expected ' + str(key) + ' is '
                                      + str(response_must[key]) + '; Actuality is ' + str(temp[key]))
                        except KeyError:
                            self.flag = True
                            tolog('Fail: Missing parameter ' + str(key))
                    else:
                        tolog('HTTP status code is ' + str(result['response']))
                        tolog(json.dumps(temp, ensure_ascii=False, indent=2).replace('\n', ''))
                        tolog('-*- The case is executed! -*-\n')

                optional_settings[p] = p_value
                optional_settings['sign'] = pay_key

                time.sleep(hold_time)

        if self.flag:
            tolog(Fail)
        else:
            tolog(Pass)

    # For failed test of method  'post/put/delete' and confirm response
    def failed_settings_test(self, cases_sheet, response_sheet, hold_time=0):
        # Open cases file
        data = xlrd.open_workbook(self.cases_file)
        table1 = data.sheet_by_name(cases_sheet)
        table2 = data.sheet_by_name(response_sheet)

        for j in range(3, table1.nrows):

            # Building body parameters
            settings = dict((table1.cell(1, i).value, table1.cell(j, i).value) for i in range(1, table1.ncols))
            expected = dict((table2.cell(1, i).value, table2.cell(j, i).value) for i in range(1, table2.ncols))

            # Conversion data or data type
            handling(settings)
            if 'pp_trade_no' in settings.keys() and self.service == 'api/scannedCode':
                num = random.randint(1, 100)
                settings['pp_trade_no'] = str(num) + str(settings['pp_trade_no'])
            if 'sign' in settings.keys():
                t = settings['sign']
                settings.pop('sign')
                settings['sign'] = jm(settings, str(t))

            handling(expected)

            # write log
            tolog('Checkpoint: ' + str(table2.cell(j, 0).value))
            tolog('Body: ' + json.dumps(settings, ensure_ascii=False, indent=2).replace('\n', ''))
            tolog('Expected Response: ' + json.dumps(expected, ensure_ascii=False, indent=2).replace('\n', ''))

            # Sending request
            result = server.webapi(self.method, self.serverIp, self.service, settings)

            if str(result['response']) == '<Response [500]>':
                self.flag = True
                tolog('Fail: HTTP status code is ' + str(result['response']))
                tolog('Error Message: ' + str(result['text']).replace('\n', ''))
                tolog('-*- The case is executed! -*-\n')
            else:
                temp = json.loads(result["text"])
                for key in expected.keys():
                    try:
                        if str(expected[key]) != '' and str(expected[key]) not in str(temp[key]):
                            self.flag = True
                            tolog('Fail: Expected ' + str(key) + ' is ' + str(expected[key]) + '; Actuality is ' + str(temp[key]))
                    except KeyError:
                        self.flag = True
                        tolog('Fail: Missing parameter ' + str(key))

                tolog('HTTP Status Code: ' + str(result['response']))
                tolog('Actual Response: ' + json.dumps(temp, ensure_ascii=False))
                tolog('-*- The case is executed! -*-\n')

            time.sleep(hold_time)

        # test must parameters
        r_m_settings = dict((table1.cell(1, i).value, table1.cell(2, i).value) for i in range(1, table1.ncols))

        if len(self.must) != 0:
            for p in self.must:
                must_value = r_m_settings.pop(p)

                # Conversion data or data type
                handling(r_m_settings)

                if 'pp_trade_no' in r_m_settings.keys() and self.service == 'api/scannedCode':
                    num = random.randint(1, 100)
                    r_m_settings['pp_trade_no'] = str(num) + str(r_m_settings['pp_trade_no'])
                if 'sign' in r_m_settings.keys():
                    t = r_m_settings['sign']
                    r_m_settings.pop('sign')
                    r_m_settings['sign'] = jm(r_m_settings, str(t))

                # Expected result
                tolog('\nRemove must parameter: ' + str(p))
                tolog('Body: ' + json.dumps(r_m_settings, ensure_ascii=False, indent=2).replace('\n', ''))

                # Sending request
                result = server.webapi(self.method, self.serverIp, self.service, r_m_settings)

                if str(result['response']) == '<Response [500]>':
                    self.flag = True
                    tolog('Fail: HTTP status code is ' + str(result['response']))
                    tolog('Error Message: ' + str(result['text']).replace('\n', '') + '\n')
                else:
                    temp = json.loads(result["text"])
                    try:
                        if type(temp['code']) == str and temp['code'] != 'FAIL':
                            self.flag = True
                            tolog('Fail: Please check out "code" value')
                        elif type(temp['code']) == int and temp['code'] != 201:
                            self.flag = True
                            tolog('Fail: Please check out "code" value')
                        elif 'msg' in list(temp.keys()) and temp['msg'] == '':
                            self.flag = True
                            tolog('Fail: "msg" is empty')
                        elif 'message' in list(temp.keys()) and temp['message'] == '':
                            self.flag = True
                            tolog('Fail: "message" is empty')
                    except KeyError:
                        tolog('\nPlease change the inspection conditions!!!\n')

                    tolog('HTTP Status Code: ' + str(result['response']))
                    tolog('Actual Response: ' + json.dumps(temp, ensure_ascii=False))
                    tolog('-*- The case is executed! -*-\n')
                
                r_m_settings[p] = must_value
                time.sleep(hold_time)

        if self.flag:
            tolog(Fail)
        else:
            tolog(Pass)