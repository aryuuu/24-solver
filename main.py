#!/usr/bin/python
# import itertools
import time
#get four positive integers from user input
#user's input is assumed to be always possitive
def getfour():
	raw = raw_input()
	four = raw.split(' ')
	four = [c+'.0' for c in four] 
	return four

# amin = getfour()
# print sum(amin)

#we will be using eval() to get result from the string



# result = set(itertools.permutations(sauce))
# print len(result)
# print result



#read the four and get all possible combinations

# combs = set(itertools.permutations(sauce))
sauce = getfour()
combs = []

#get starting time
start = time.time()

for a in range(len(sauce)):
	for b in range(len(sauce)):
		for c in range(len(sauce)):
			for d in range(len(sauce)):
				if(a == b or a == c or a == d or b == c or b == d or c == d):
					continue
				temp = []
				temp.append(sauce[a])
				temp.append(sauce[b])
				temp.append(sauce[c])
				temp.append(sauce[d])
				combs.append(temp)

# print len(combs)


#creating all possible repeated permutation of operators

# opcombs = [p for p in itertools.product(ops, repeat=3)]
# print opcombs
# print len(opcombs)
ops = ['+', '-', '*', '/']
opcombs = []

for a in ops:
	for b in ops:
		for c in ops:
			temp = []				
			temp.append(a)
			temp.append(b)
			temp.append(c)
			opcombs.append(temp)

# print len(opcombs)

results = []

for comb in combs:
	for i in range(4): #loop for parentheses
		#patterns of parentheses
		#(ab)(cd)
		#(a(bc))d
		#((ab)c)d
		#a((bc)d) 
		if i == 0:
			for op in opcombs:
				expression = '(' + comb[0] + op[0] + comb[1] + ')' + op[1] + '(' + comb[2] + op[2] + comb[3] + ')'
				try:
					if eval(expression) == 24 and expression not in results:
						results.append(expression)
				except:
					pass
		elif i == 1:
			for op in opcombs:
				expression = '(' + comb[0] + op[0] + '(' + comb[1]  + op[1] + comb[2] + '))' + op[2] + comb[3] 
				try:
					if eval(expression) == 24 and expression not in results:
						results.append(expression)
				except:
					pass
		elif i == 2:
			for op in opcombs:
				expression = '((' + comb[0] + op[0] + comb[1] + ')' + op[1] + comb[2] + ')' + op[2] + comb[3] 
				try:
					if eval(expression) == 24 and expression not in results:
						results.append(expression)
				except:
					pass
		elif i == 3:
			for op in opcombs:
				expression = comb[0] + op[0] + '((' + comb[1]  + op[1] + comb[2] + ')' + op[2] + comb[3] + ')'
				try:
					if eval(expression) == 24 and expression not in results:
						results.append(expression)
				except:
					pass


#get finish time
end = time.time()


if len(results) > 0:
	print 'we got ' + str(len(results)) + ' results for that'

	for result in results:
		print result
else:
	print "we ain't got any bro"

print "the whole process takes " + str(end-start) + " seconds"