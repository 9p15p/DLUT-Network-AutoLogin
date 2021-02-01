#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 下午2:04
# @Author  : Merci
# @mail    : Merci@mail.dlut.edu.cn
# @File    : test_version.py
from selenium import webdriver
import time

def main():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.quit()

if __name__ == '__main__':
    main()