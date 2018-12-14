def calc_n():
	p = input("Enter p: ")
        q = input("Enter q: ")
        n = p*q
        print n

def calc_c():
	e = input("Enter e: ")
	m = input("Enter m: ")
	n = input("Enter n: ")
	c = (m**e) % n
	print c

def calc_m():
	message = input("Enter message: ")
	print int(message.encode("hex"), 16)

def calc_tot():
	p = input("Enter p: ")
	q = input("Enter q: ")
	tot = (p-1)*(q-1)
	print tot

#D calculation is work in progress
#def calc_d():
#	e = input("Enter e: ")
#	p = input("Enter p: ")
#	q = input("Enter q: ")
#	n = (p-1)*(q-1)
#	d = (1/e) % n
#	print d

while True:
	mode = input("Choose what to calculate, (n=1, m=2, c=3 tot=4):" )
	if mode is 1:
		calc_n()

	elif mode is 3:
		calc_c()

	elif mode is 2:
		calc_m()

	elif mode is 4:
		calc_tot()

#D calculation is work in progress
#	elif mode is 5:
#		calc_d()
