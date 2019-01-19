#!/usr/bin/python
import itertools
#get four positive integers from user input
def getfour():
	raw = raw_input()
	four = raw.split(' ')
	four = [c for c in four]
	return four

# amin = getfour()
# print sum(amin)

#we will be using eval() to get result from the string



# result = set(itertools.permutations(sauce))
# print len(result)
# print result



#read the four and get all possible combinations
sauce = getfour()
combs = set(itertools.permutations(sauce))

results = []


#creating all possible repeated permutation of operators
ops = ['+', '-', '*', '/']
opcombs = [p for p in itertools.product(ops, repeat=3)]
# print opcombs

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
					if eval(expression) == 24:
						results.append(expression)
				except:
					pass
		elif i == 1:
			for op in opcombs:
				expression = '(' + comb[0] + op[0] + '(' + comb[1]  + op[1] + comb[2] + ')' + ')' + op[2] + comb[3] 
				try:
					if eval(expression) == 24:
						results.append(expression)
				except:
					pass
		elif i == 2:
			for op in opcombs:
				expression = '(' + '(' + comb[0] + op[0] + comb[1] + ')' + op[1] + comb[2] + ')' + op[2] + comb[3] 
				try:
					if eval(expression) == 24:
						results.append(expression)
				except:
					pass
		elif i == 3:
			for op in opcombs:
				expression = comb[0] + op[0] + '(' + '(' + comb[1]  + op[1] + comb[2] + ')' + op[2] + comb[3] + ')'
				try:
					if eval(expression) == 24:
						results.append(expression)
				except:
					pass


if len(results) > 0:
	print 'we got ' + str(len(results)) + ' results for that'

	for result in results:
		print result
else:
	print "we ain't got any bro"