import sys
import copy
import time
from operator import itemgetter
st=time.time() 				#store the time at which program execution begins
sys.setrecursionlimit(15000)		


#function to check the presence of contradiction in a given array (if both- the literal and it's negative form- are present)

def negcheck(a):
	for i in range(len(a)):
		for j in range(i,len(a)):
			if(i!=j):
				x=a[i]
				y=a[j]
				if(x+y==0):                             #if a literal exists in it's positive as well as negative for
					return 0			#return 0


	return 1				#if no such literal is found then return 1

#function which will remove all the clauses from 'arr' that have presence of 'b' and drop '-b' from clauses of length > 1

def opt(arr,b):
	ret=[]
	for i in range(len(arr)):
		if(b in arr[i]):
			arr[i]=['#']			#find all the clauses containing 'b' mark them as '#'
		if(-b in arr[i] and len(arr[i])>1):
			if(arr[i].count('*')==(len(arr[i])-1)):
				continue
			else:
				arr[i][arr[i].index(-b)]='*'		#Find presence of '-b' in clauses of length >1 and mark it as '*'


	for i in range(len(arr)):			#loop to drop everything that is marked '#' or '*'
		if(arr[i]==['#']):
			continue
		elif('*' in arr[i]):
			s=[]
			for j in range(len(arr[i])):
				if(arr[i][j]!='*'):
					s.append(arr[i][j])
				else:
					continue
			ret.append(s)
		else:
			ret.append(arr[i])
	return ret

#function that will perform unit propogation on the given array
def answer(a):
	with open('out.txt','w') as f1: 						
		#c=f.readlines()
		f1.write("SAT\n")	
		for i in range(len(a)):
			n=a[i]
			f1.write(str(n)+" ")


def makesing(arr,solution):
	rem=[]
	for i in range(len(arr)):
		if(len(arr[i])==1):
			rem.append(arr[i][0])

	for i in range(len(rem)):
		solution.append(rem[i])
		arr=opt(arr,rem[i])
		
	return arr
			


decomp=0                  				 #global variable that will keep count of number of decompositions

	
#recursive function to check for a solution
def sol(inp,solution,dex):                  #dex is the number of literals that have been assigned a value so far  
 
	global decomp
	decomp=decomp+1				#update number of decompositons by 1 every time we enter the function
	print("Length of solution array: ",len(solution))

	dex2=copy.deepcopy(dex)
	dex2=dex2+1				#update the number of literals assigned a value so far by +1


	if(negcheck(solution)==0):		#if contradiction is present in the solution then return
		return

	if(len(inp)==0 and negcheck(solution)==1):  #if input array has become empty and no contradiction is there in the solution array then we have found our required solution; print and exit

		solution=sorted(solution,key=abs)		#sorting the solution array by the order of the absolute values of literals
		solfin=[]					#solfin will contain the solution after removing the multiple occurences of a single literal in solution array
		for i in range(len(solution)):
			if(solution[i] not in solfin):
				solfin.append(solution[i])
		print("Length of solution array: ",len(solfin))	

		print("SOLUTION FOUND",solfin)			#print the solution
		print ("TIME TAKEN",time.time()-st)		#print the amount of time taken(in seconds) to solve the cnf formula
		answer(solfin)		
		sys.exit()				#stop the program execution

	global var
	for i in range(dex,len(var)):
		rem2=-var[i]				#assign false to the current literal in consideration, add it to the solution array and do the recursion call
		dummy2=copy.deepcopy(solution)
		dummy2.append(rem2)
		q2=copy.deepcopy(inp)
		q2=opt(q2,rem2)
		q2=makesing(q2,dummy2)			#applying unit propogation on the input array
		sol(q2,dummy2,dex2)
		
		rem=var[i]				#assign true to the current literal in consideration, add it to the solution array and do the recursion call
		dummy=copy.deepcopy(solution)	
		dummy.append(rem)
		q=copy.deepcopy(inp)
		q=opt(q,rem)
		q=makesing(q,dummy)			#applying unit propogation on the input array
		sol(q,dummy,dex2)

		return				#if no solution is found after assigning both true and false to the current variable then return back




								


inp=[]                                        #array that will contain the cnf form of the input text file as a list of lists  



#reading from the input text file and appending in the 'inp' array   
with open('input.txt','r') as f: 						
	c=f.readlines()	
	for i in range(1,len(c)):
		n=c[i]
		k=n.split()
		for n in range(len(k)):
			k[n]=int(k[n])
		inp.append(k[:-1])
print("INPUT ARRAY",inp)

inp=sorted(inp,key=itemgetter(0))               #sorts clauses in the order of their first literal; explained in heuristics
inp=inp[::-1]
var=[]	    #array that will store all the literals that appear in the cnf file

for i in range(len(inp)):
	for j in range(len(inp[i])):
		if(inp[i][j] in var or -inp[i][j] in var ):
			continue
		else:
			var.append(abs(inp[i][j]))
var=var[::-1]


solution=[]					#array that will contain our solution

inp=makesing(inp,solution)
sol(inp,solution,0)			#solution function call
print("UNSAT")
with open('out.txt','w') as f1: 						
	f1.write("UNSAT\n")
