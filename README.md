# 大连理工大学自动联网脚本

## requirements
```shell
pip install selenium
pip install pillow

sudo apt-get install chromium-chromedriver
#最后一条命令如有报错，请自行上网查看解决方案

#验证码版本似乎是不必要的，如需使用请
#记得装pytesseract和tesseract-ocr
#并取消注释相关代码片段
```
## 在代码中添加你的账号密码
```python
#e.g.

username = "22009549"  # 此处输入网络认证账号
password = "abcdefgh"  # 此处输入网络认证密码
```

## how to use
开机后，用screen后台运行
或者直接打开个终端一直运行【保证它不被关闭】

## 关于开机自启
有心的同学可自行研究，我觉得不会断网和断电同时到来。

## 感谢原作者
https://github.com/anruoran/Network-State-Detection-and-AutoLogin
