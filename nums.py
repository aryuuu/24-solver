#!/usr/bin/python

num = '1 2 3 4'
num = num.split(' ')

results = []

for a in num:
	for b in num:
		for c in num:
			for d in num:
				temp = []
				temp.append(a)
				if(b in temp):
					continue
				temp.append(b)
				if(c in temp):
					continue
				temp.append(c)
				if(d in temp):
					continue
				temp.append(d)
				if(temp in results):
					continue
				results.append(temp)

print len(results)

for result in results:
	print result