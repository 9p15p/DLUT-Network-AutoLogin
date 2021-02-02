#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 下午2:04
# @Author  : Merci
# @mail    : Merci@mail.dlut.edu.cn
# @File    : test_version.py
from selenium import webdriver
import time
import sys
def main():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.quit()

    user_passwd_txt = sys.argv[0].replace('test_version.py', 'user_passwd.txt')
    f = open(user_passwd_txt)
    username = f.readline()[9:-1]
    password = f.readline()[9:-1]
    print('username: ',username)
    print('password: ',password)

if __name__ == '__main__':
    main()