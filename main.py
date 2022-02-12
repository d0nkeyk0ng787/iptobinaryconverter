#! /usr/bin/env python3

# Written by D0nkeyk0ng787
# Simple program that can convert an ip address into its binary version
# Wrote this more for the sake of it rather then to serve any real purpose

def createBinaryIP(binarylist):
	sep = "."
	x = sep.join(binarylist)
	print(x)


def main():

	active = True
	ui = input("Enter a valid IP address you wish to convert to binary: ")
	#ui = "192.168.100.100"

	while active:
		uisplit = ui.split('.', 4)
		bi = []
		for i in range(len(uisplit)):

			l = [] 
			l.append(uisplit[i])

			for j in range(len(l)):

				ti = int(l[j])
				dtb = bin(ti)
				
				bi.append(dtb.replace("0b", ""))
		createBinaryIP(bi)
		break

if __name__ == '__main__':
	main()

