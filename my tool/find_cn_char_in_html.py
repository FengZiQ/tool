# coding=utf-8
import re
from batch_change_char import list_files


def find_cn_char(file, char_file):
    content = []
    for line in open(file, 'r', encoding='utf-8'):
        if '//' not in line:
            m = re.findall('[\u4e00-\u9fa5]+', line)
            if len(m):
                content += m
    temp = set(content)
    for s in temp:
        print(s)
        with open(char_file, 'a', encoding='utf-8') as f:
            f.write(s+'\n')


if __name__ == "__main__":
    for file in list_files('D:/BaiduNetdiskDownload/components'):
        find_cn_char(
            file,
            file + '.txt',
        )
