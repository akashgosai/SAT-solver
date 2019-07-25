import itertools
import os
import random

sudoko=[]               		 #sudoko will be stored in the form of array of strings
with open('enter.txt','r') as f1:
	string=''
	n=0	
	l=''
	line=f1.readlines()
	i=0
	while(i!=9):	
		
		s=''	
		l=line[i]	
		for j in range(9):
			s=s+l[j]
		sudoko.append(s)
		i=i+1
	

clauses=[]				#array to store the clauses which will be feeded to the minisat solver

def number(i,j,k):	    	        #function to make the corresponding preposition when k is stored in (i,j) cell
	 return 100*i+10*j+k

def once(prep):				#a function to check that a number occurs at max once in a cell and all are distinct 
	clauses.append([l for l in prep])
	for p in itertools.combinations(prep,2):
		clauses.append([-l for l in p])

for i in range(1,10):
	for j in range(1,10):
		prep=[]
		for k in range(1,10):
			prep.append(number(i,j,k))     #EXACTLY one number in a cell
		once(prep)
		
for i in range(1,10):
	for k in range(1,10):
		prep=[]
		for j in range(1,10):
			prep.append(number(i,j,k))      #EXACTLY one number in a column
		once(prep)		

for j in range(1,10):
	for k in range(1,10):
		prep=[]
		for i in range(1,10):
			prep.append(number(i,j,k))       #EXACTLY one number in a row
		once(prep)


for i in range(1,10,3):
	for j in range(1,10,3):
		for k in range (1,10): 			#EXACTLY one number in a 3x3 block
			once([number(i+i1,j+j1,k) for (i1, j1) in itertools.product (range(3),repeat=2)])

for j in range(1,10):
	prep=[]
	for k in range(1,10):
		prep.append(number(j,10-j,k))     	#EXACTLY one number in the main diagonal
	once(prep)

for a in range(1,10):
	for b in range(1,10):
		for k in range(1,10):
			if(a!=b):
				x=number(a,10-a,k)
				y=number(b,10-b,k)
				clauses.append([-x,-y])		#EXACTLY one number in the main diagonal



for a in range(1,10):
	for b in range(1,10):
		for k in range(1,10):
			if(a!=b):
				x=number(a,a,k)
				y=number(b,b,k)
				clauses.append([-x,-y])


for i in range(0,9):
	for j in range(0,9):
		if(sudoko[i][j]!='.'):
			clauses.append(number(i+1,j+1,int(sudoko[i][j])))	#adding corresponding clauses for the already filled cells


with open('input.txt','w') as f: 						#writing the clauses on the input file that will be feeded into minisat solver
	f.write("p cnf {} {} \n".format(999,len(clauses)))
	for c in (clauses):
		c=str(c)
		for p in c:
			if (p!='[' and p!=']' and p!=','):		
				f.write("".join(p))
		f.write(" 0\n")


os.system("minisat input.txt output.txt")				#solving the sudoko based on the input clauses

with open('output.txt','r') as f1:
	f2=''
	for c in f1:
		if(c=='SAT\n'):
			continue
		else:
			for c1 in c:
				f2=f2+("".join(c1))
			f2=f2+("\n")
	flag=0
	final=''						#final is the string that will store all the positive prepositions
	for i in range(0,len(f2)-3):
		if(f2[i]=='-'):
			flag=1
		if(f2[i]==' '):
			flag=0
		if(flag==0 and f2[i+1]!='-'):
			final=final+f2[i+1]
	
	n=0
	for i1 in range(2,len(final)-2,4):
		n=n+1
		if (n!=9):		
			print(final[i1] ,end=" ")

		else:
			print(final[i1])
			n=0
		
		
			


	


