#!/usr/bin/env python

data=open("datafile.txt","w+")

for i in range(10):
     data.write("This is line %d\r\n" % (i+1))

data.close()

data=open("datafile.txt","a+")

for i in range(2):
     data.write("Appended line %d\r\n" % (i+1))

data.close()

data=open("datafile.txt", "r")

isi=data.read()
print(isi)


data.close()
