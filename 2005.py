#!/usr/bin/python
#coding=utf-8
from pexpect import pxssh

def send_command(s,cmd):

	s.sendline(cmd)
	#匹配prompt(提示符)
	s.prompt()
	#将prompt前所有内容打印出
	print s.before

def connect(host,user,password):
	try:
		s = pxssh.pxssh()
		#利用pxssh类的login()方法进行ssh登录
		s.login(host,user,password)
		return s
	except:
		print '[-] Error Connecting'
		exit(0)

s = connect('10.10.10.128','msfadmin','msfadmin')
send_command(s,'uname -a')