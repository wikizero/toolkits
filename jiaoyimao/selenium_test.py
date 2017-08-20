# coding:utf-8
import wget
import pdir
import colorama
def func():
	print colorama.Fore.BLUE,'done....'
response = wget.download('https://www.zhihu.com/#signin', out='zhuhu.html', bar=func())

print ''