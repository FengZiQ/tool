# coding = utf-8
import os, shutil


def rename():

    files_path = r"D:\debug\图片\\"

    for (dirPath, dirs, files) in os.walk(files_path):

        for f in files:
            if '.bmp' in f and len(f) == 9:
                shutil.move(files_path + f, files_path + f[:5] + 'a' + f[-4:])
            elif '.bmp' in f and len(f) == 10:
                shutil.move(files_path + f, files_path + f[:6] + 'a' + f[-4:])

    for (dirPath, dirs, files) in os.walk(files_path):

        for f in files:
            if '1a' in f and len(f) == 10:
                shutil.move(files_path + f, files_path + f[:4] + '2' + f[-4:])
            elif '1a' in f and len(f) == 11:
                shutil.move(files_path + f, files_path + f[:5] + '2' + f[-4:])
            elif '2a' in f and len(f) == 10:
                shutil.move(files_path + f, files_path + f[:4] + '1' + f[-4:])
            elif '2a' in f and len(f) == 11:
                shutil.move(files_path + f, files_path + f[:5] + '1' + f[-4:])


if __name__ == "__main__":
    rename()