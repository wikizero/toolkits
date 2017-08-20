# coding:utf-8
import re

ss = '''
abc aaaaa
123 abc 444
'''

def func(s):
	return  s.group()*2

print re.sub(r'abc(.*)',func, ss)
