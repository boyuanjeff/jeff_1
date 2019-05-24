# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 11:12
# @Author  : 周博远
# @Email   : boyuanky@gmail.com
# @File    : a.py
# @Software: PyCharm


def chigutou(a="dog"):
    print("%s 吃骨头"%a)





class Gou(object):

    def chigutou(self):

        print("吃骨头")

    def chishi(self):
        print("吃屎")

if __name__ == "__main__":
    gou = Gou()
    gou.chigutou()
    chigutou()