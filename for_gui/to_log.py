# coding = utf-8

import time


def tolog(strinfo):
        if strinfo != "'result': 'p'" or strinfo != "'result': 'f'":
            with open("gui_scripts.log", "r+", encoding='UTF-8') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(time.time())) + ": " + strinfo + '\n' + content)

                f.close()
            print(strinfo)
        # for testlink steps populate
        fout = open("testLink.notes", "a", encoding='UTF-8')
        fout.write(strinfo + '\n')

        fout.close()


