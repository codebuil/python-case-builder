#!/usr/bin/python
print("\033c\033[42;30m\n");
n=raw_input('enumerate cases in ');
print();
print ("switch var1{");
ss=n.split(",");
for nn in range(0,len(ss)):
	print ("\tcase \""+ss[nn]+"\":");
	print ("\t//code");
print"\tdefault:\n\t//\n}\n"


