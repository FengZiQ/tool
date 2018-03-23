# coding = utf-8
import os, shutil
import time


def rename(path='D:\debug\picture\\'):

    first = str(input('Please input first file name: ')) + '.bmp'
    new_name = ''
    count = 0
    while True:
        for (dirPath, dirs, files) in os.walk(path):
            s = []
            for f in files:
                if first[:2] in f and f[3] == '-':
                    s += [int(f[2])]
                elif first[:2] in f and f[3] != '-':
                    s += [int(f[2:4])]
            s.sort()
            for f in files:
                if '.bmp' in f:
                    if first[:2] not in f and len(s) == 0:
                        shutil.move(path + f, path + first)
                        count += 1
                        print ("Di " + str(count))
                        continue
                        time.sleep(5)
                    elif first[:2] not in f and len(s) <= 9:
                        new_name += first[:2] + str(s[-1] + 1) + first[3:5] + '.bmp'
                        shutil.move(path + f, path + new_name)
                        new_name = ''
                        count += 1
                        print ("Di " + str(count))
                        continue
                        time.sleep(5)
                    elif first[:2] not in f and len(s) > 9:
                        new_name += first[:2] + str(s[-1] + 1) + first[3:5] + '.bmp'
                        shutil.move(path + f, path + new_name)
                        new_name = ''
                        count += 1
                        print ("Di " + str(count))
                        continue
                        time.sleep(5)
                    else:
                        continue

if __name__ == "__main__":
    rename()