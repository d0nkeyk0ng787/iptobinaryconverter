#! /usr/bin/env python3

# Simple program that can convert an ip address into its binary version
# I wrote this more for the sake of it then to serve any real purpose as it's quicker to do this in your head
# WORK IN PROGRESS

def converttobinary(iplist):
	pass

def main():

	active = True
	ui = input("Enter a valid IP address you wish to convert to binary: ")

	while active:
		uisplit = ui.split('.', 4)
		#uireplace = ui.replace('.', '')
		#print(uisplit)
		for i in range(len(uisplit)):
			#print(uisplit[i])
			l = [] 
			l.append(uisplit[i])
			#print(l)

			for i in range(len(l)):
				#toint = int(l[i])
				#print(l[i])
				ti = int(l[i])
				#print(ti)
				#dtb = bin(ti.replace("0b",""))
				dtb = bin(ti)
				print(dtb.replace("0b",""))
			#print(l)
			#toint = int(uisplit[i])
			#print(toint)
			#dtb = bin(toint.replace("0b",""))

		break

if __name__ == '__main__':
	main()

