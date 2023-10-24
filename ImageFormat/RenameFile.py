import multiprocessing
import os
import argparse
import time


# path = input('请输入文件路径(结尾加上/)：')
# Transfer img and target to have the same name
# 获取该目录下所有文件，存入列表中

def Rename(fileList):
    for file in fileList:
        # 设置旧文件名（就是路径+文件名）
        oldname = path + os.sep + file  # os.sep添加系统分隔符
        # 设置新文件名
        newname = path + os.sep + file.replace("568", "Retardance")
        os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
        print(oldname, '======>', newname)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run this renamefile for transfer images' name ")
    parser.add_argument('--path', type=str, default='./', help='give a path to find images')
    args = parser.parse_args()
    path = args.path
    fileList = os.listdir(path)

    # 多线程
    start = time.time()
    p = multiprocessing.Pool(8)
    p.map(Rename, fileList)
    p.close()
    end = time.time()
    print(end - start, 's')
