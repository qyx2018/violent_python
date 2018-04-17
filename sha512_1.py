import passlib.hash, crypt

ctype = "6" #for sha512 (see man crypt)
salt = "qwerty"
insalt = '${}${}$'.format(ctype, salt)
password = "AMOROSO8282"

value1 = sha512_crypt.encrypt(password, salt=salt, rounds=5000)
value2 = crypt.crypt(password, insalt)
if not value1 == value2:
    print("algorithms do not match")
print("{}\n{}\n\n".format(value1, value2))