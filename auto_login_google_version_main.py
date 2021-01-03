# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:40:17 2019

@author: xia
"""

import time
from selenium import webdriver
import socket


def isNetOK(testserver):
    s=socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

def isNetChainOK(testserver=('www.baidu.com',443)):
    isOK = isNetOK(testserver)
    return isOK

def isThereValidCode():
    isThereValidCode = "block" in browser.find_element_by_id("isDisplayValidCode").get_attribute('style')
    return isThereValidCode

while 1:

    isOK = isNetChainOK()  # 网络连通性测试

    if isOK==True:
        date_time = time.asctime(time.localtime(time.time()));
        print("当前网络处于连通状态 " + date_time)

    elif isOK==False:
        date_time = time.asctime(time.localtime(time.time()));
        print("当前没网 " + date_time)

        url = "http://auth.dlut.edu.cn/"  # 如 https://10.108.255.12
        username = "22009549"  # 此处输入网络认证账号
        password = "nasdjs12"  # 此处输入网络认证密码

        # 关闭浏览器的信息提示，解决“Chrome正在收到自动测试软件的控制”遮蔽问题
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        browser = webdriver.Chrome(options=option)  # 打开浏览器
        # browser.minimize_window()  # 最小化浏览器

        browser.get(url)
        browser.implicitly_wait(10)
        # 等待网页加载完毕（隐式等待），避免因网页未加载完成查找不到所需元素出现异常

        name_input = browser.find_element_by_id("username")         # 找到用户名的id
        name_input_tip = browser.find_element_by_id("username_tip") # 找到用户名的id的文本框

        pass_input = browser.find_element_by_id("pwd")              # 找到输入密码的id
        pass_input_tip = browser.find_element_by_id("pwd_tip")      # 找到输入密码的id的文本框

        login_button = browser.find_element_by_id("SLoginBtn_1")    # 找到登录按钮的id

        name_input_tip.click()              # 点击文本框，清空用户名框中的已有信息
        name_input.send_keys(username)      # 填入用户名
        time.sleep(0.2)
        pass_input_tip.click()              # 点击密码, 清空密码框中的已有信息
        pass_input.send_keys(password)      # 填入密码
        time.sleep(0.2)

        # # 测试中发现，验证码部分可无。
        # # 如需使用，记得装pytesseract和tesseract-ocr
        # if isThereValidCode():
        #     import pytesseract        
        #     from PIL import Image,ImageEnhance
        #     vaild_code = browser.find_element_by_id("validCode")        # 找到验证码的id
        #     vaild_code_tip = browser.find_element_by_id("validCode_tip")# 找到验证码的id的文本框
        #     valid_Image= browser.find_element_by_id("validImage")       # 验证码图片
        #     h = valid_Image.rect['height']
        #     w = valid_Image.rect['width']
        #     x = valid_Image.rect['x']
        #     y = valid_Image.rect['y']
        #     browser.save_screenshot("screenshot.png")
        #
        #     # 3、打开截图，获取验证码位置，截取保存验证码
        #     ran = Image.open("screenshot.png")
        #     box = (x, y, x+w, y+h)   # 获取验证码位置,自动定位，代表（左，上，右，下）
        #     validcode_pure_img = ran.crop(box)
        #     validcode_pure_img.save("validcode.png")
        #     validcode_contrast_add = ImageEnhance.Contrast(validcode_pure_img).enhance(2.0) #二值增强
        #     validcode_contrast_add.save("validcode_contrast_add.png")
        #     code = pytesseract.image_to_string(validcode_contrast_add).strip()
        #     vaild_code_tip.click()  # 点击文本框，清空验证码框中的已有信息
        #     vaild_code.send_keys(code)  # 填入验证码
        #     time.sleep(0.2)

        # 解决因网络连通性检测异常导致的非断网状态下登陆报错问题
        try:

            login_button.click()  # 点击登录

        except (KeyboardInterrupt, SystemExit):

            # user wangts to quit
            raise  # reraise back to caller

        except Exception:

            print('非断网状态下异常登陆')

        # time.sleep(0.2)
        # print(browser.get_cookies())

        time.sleep(2)
        print(browser.title)

        browser.close()
        browser.quit()

    # time.sleep(300)  # 每隔一段时间检测一次当前网络连通性，该时间间隔可根据需要修改
    time.sleep(3)  # 每隔一段时间检测一次当前网络连通性，该时间间隔可根据需要修改
