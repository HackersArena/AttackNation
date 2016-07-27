import md5

def simple_md5():
	counter = 1
	pass_found = False

	pass_in = raw_input("Please enter md5 hash: ")
	pwfile = raw_input("Please enter the password file name:  ")

	try:
		pwfile = open(pwfile , "r")
	except:
		print "\nFile not Found"
		quit()

	for password in pwfile:
		filemd5 = md5.new(password.strip()).hexdigest()
		print "[+]Trying password number %d:%s" % (counter, password.strip())

		counter += 1

		if pass_in == filemd5:
			print "Password found : %s" % (password)
			break



def interact():
    simple_md5()
    return
