foo=raw_input("condition :")

#import pdb;pdb.set_trace()
sum=0
for i in foo:
	#print i.isdigit()
	if i.isdigit()==True:
		print i
		sum+=int(i)
print sum

