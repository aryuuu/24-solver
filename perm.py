#!/usr/bin/python
# import itertools
raw = '+ - * /'
raw = raw.split(' ')

results = []

for a in raw:
	for b in raw:
		for c in raw:
			temp = []				
			temp.append(a)
			temp.append(b)
			temp.append(c)
			results.append(temp)
			# if temp not in results:
			# 	results.append(temp)

print len(results)
# alt = [p for p in itertools.product(raw, repeat=3)]
# print len(alt)
# for i in results:
# 	print i