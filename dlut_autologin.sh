#!/bin/bash 
source ~/anaconda3/bin/activate Network
python $(cd `dirname $0`; pwd)/dlut_autologin.py
