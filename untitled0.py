# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hZIPQAKtkubNWDfI_tk5S4CBwEbP58ao
"""

x=5
print(f"變數x的值是:{x}")
print(f"變數x的記憶體地址是:{id(x)}")

hight=float(input("請輸入您的身高(公尺):"))
weight=float(input("請輸入您的體重(公斤):"))
BMI=weight/(hight**2)
print(f"您的BMI是:{BMI:.2f}")