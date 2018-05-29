
import matplotlib.pyplot as plt
import numpy as np 
import time

vipfile = open('VIPdata.txt','r')
fig,ax=plt.subplots()


people_lib = []
people_times = []
a = 0
for i in vipfile.readlines():
	b1,b2,b3,b4,b5 = i.split()
	people_lib.append(b1)
	print(b1)


print(people_times)



while(1):
	logfile  = open('log.txt','r')
	people = []
	people_times = []
	for line in logfile.readlines():
		a1,a2,a3 = line.split()
		people.append(a3)
	logfile.close()	
	

	for i in people_lib:
		people_times.append(people.count(i))
	people_times.append(len(people))
	print(people_lib,people_times)
	people_lib.append('All')
#
	ax.cla()
	ax.bar(people_lib,label='test',height=people_times,width=0.3)
	ax.legend()
	plt.pause(1)



vipfile.close()
logfile.close()


