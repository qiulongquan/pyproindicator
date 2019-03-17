
import os, sys


class redirection():
    def __init__(self):
        self.buf = ''
        self.__console__ = sys.stdout
        self.path = 'd:\\'  # 存放日志的路径

    def write(self, output_stream):
        self.buf += output_stream

    def to_log(self, filename):
        # file = open(self.path+filename, 'w+')
        file = open(self.path+filename, "w")
        sys.stdout = file
        print(self.buf)
        file.close

    def to_console(self):
        sys.stdout = self.__console__
        print(self.buf)

    def flush(self):
        self.buf = ''


def main():
    obj = redirection()
    input_stream = input("输入：")
    while input_stream:  # 实现循环输入
        obj.write(input_stream + '\n')
        input_stream = input("输入：")
    obj.to_log('log.txt')  # 日志名称为log.txt
    obj.to_console()
    obj.flush()


if __name__ == "__main__":
    main()
