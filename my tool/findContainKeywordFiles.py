# coding=utf-8
import os


def find_file(keyword, path):
    res = []
    for cur_path, cur_dirs, cur_files in os.walk(path):
        for file in cur_files:
            if '.txt' in file:
                try:
                    with open(path + file, 'r+', encoding='utf-8') as f:
                        content = f.read()
                        f.close()
                        if keyword in content:
                            res.append(file)
                except:
                    pass
    return res


if __name__ == "__main__":
    print(find_file('python', r'D:/script/'))
