import random
import os
import itertools

sudoko=[]
for i in range(9):
	row=[]					#creating an empty sudoko with '.' only
	for j in range(9):
		row.append(".")
	sudoko.append(row)
def ransudo():					#a function to generate a random completely solved sudoko
	sudoko=[				
	"*********",
	"*********",
	"*********",
	"*********",
	"*********",
	"*********",
	"*********",
	"*********",
	"*********"
	]
	sudoko1=[]
	for i in range(9):			
		l=[]
		for j in range(9):			
			l.append('.')
		sudoko1.append(l)

	clauses=[]				#an array that stores all the clauses 
	def number(i,j,k):			# a function to generate preposition which are in the form ijk in ith row jth column and k th digit
		 return 100*i+10*j+k			
	def once(prep):				#a function to check that a number occurs at max once in a cell and all are distinct 
		clauses.append([l for l in prep])
		for p in itertools.combinations(prep,2):
			clauses.append([-l for l in p])
	for i in range(1,10):
		for j in range(1,10):
			prep=[]
			for k in range(1,10):			#EXACTLY one number in a cell
				prep.append(number(i,j,k))
			once(prep)
		
	for i in range(1,10):					#EXACTLY one number in a column
		for k in range(1,10):
			prep=[]
			for j in range(1,10):
				prep.append(number(i,j,k))
			once(prep)		

	for j in range(1,10):
		for k in range(1,10):				#EXACTLY one number in a row
			prep=[]
			for i in range(1,10):
				prep.append(number(i,j,k))
			once(prep)


	for i in range(1,10,3):
		for j in range(1,10,3):
			for k in range (1,10):			#EXACTLY one number in a 3x3 block
				once([number(i+i1,j+j1,k) for (i1, j1) in itertools.product (range(3),repeat=2)])
	for j in range(1,10):
		prep=[]						#EXACTLY one number in the main diagonal
		for k in range(1,10):
			prep.append(number(j,10-j,k))
		once(prep)
	pp=[]
	for a in range(1,10):
		for b in range(1,10):
			for k in range(1,10):
				if(a!=b):				#EXACTLY one number in the main diagonal
					x=number(a,10-a,k)
					y=number(b,10-b,k)
					clauses.append([-x,-y])

	pp2=[]
	for a in range(1,10):
		for b in range(1,10):
			for k in range(1,10):
				if(a!=b):			
					x=number(a,a,k)
					y=number(b,b,k)
					clauses.append([-x,-y])

	for i in range(0,9):
		for j in range(0,9):
			if(sudoko[i][j]!='*'):
				clauses.append(number(i+1,j+1,int(sudoko[i][j])))
	q=random.randint(1,9)
	w=random.randint(1,9)
	e=random.randint(1,9)
	clauses.append(number(q,w,e))				#assigning random number to a random cell to form basis for a random suudoko

	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]		#randomising the order of clauses which provides a variation in minisat input variables resulting in different output every time
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	for i in range(len(clauses)-1,0,-1):
		j=random.randint(0,i)
		clauses[i],clauses[j]=clauses[j],clauses[i]
	with open('input.txt','w') as f:
		f.write("p cnf {} {} \n".format(999,len(clauses)))
		for c in (clauses):
			c=str(c)
			for p in c:
				if (p!='[' and p!=']' and p!=','):		
					f.write("".join(p))
			f.write(" 0\n")


	os.system("minisat input1.txt output1.txt")		#solving the sudoko based on random initial conditions and clauses to output a random sudoko by using minisat
	
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
		final=''
		for i in range(0,len(f2)-3):
			if(f2[i]=='-'):
				flag=1
			if(f2[i]==' '):
				flag=0
			if(flag==0 and f2[i+1]!='-'):
				final=final+f2[i+1]
		fin2=[]
		for i in range(0,len(final)-2,4):
			fin2.append(int(final[i])*100+int(final[i+1])*10+int(final[i+2]))
		
		for i in fin2:
			first=int((str(i))[0])
			second=int((str(i))[1])
			third=int((str(i))[2])
			sudoko1[first-1][second-1]=third
		return sudoko1

def clausesol(clauses):							#a function to add all the conditions of clauses to the input file to be given in the minisat as input 
	with open('inputtemp.txt','w') as f:
		f.write("p cnf {} {} \n".format(999,len(clauses)))
		for c in (clauses):
			c=str(c)
			for p in c:
				if (p!='[' and p!=']' and p!=','):		
					f.write("".join(p))
			f.write(" 0\n")
	os.system("minisat inputtemp.txt outputtemp.txt")
	with open('outputtemp.txt','r') as f1:			#returning 1 if the sudoko is satisfiable else 0
		f2=''
		for c in f1:
			if(c=='SAT\n'):
				return 1		#1 means SAT
			else:
				return 0
def solution(sudoko):				#a function to return the solution of the arguement sudoko 
	clauses=[]
	
	def number(i,j,k):	
		 return 100*i+10*j+k
	def once(prep):
		clauses.append([l for l in prep])
		for p in itertools.combinations(prep,2):
			clauses.append([-l for l in p])
	for i in range(1,10):
		for j in range(1,10):
			prep=[]					#checking all the condtions of a sudoko
			for k in range(1,10):			#EXACTLY one number in a cell
				prep.append(number(i,j,k))
			once(prep)
		
	for i in range(1,10):					#EXACTLY one number in a column	
		for k in range(1,10):
			prep=[]
			for j in range(1,10):
				prep.append(number(i,j,k))
			once(prep)		
		
	for j in range(1,10):
		for k in range(1,10):				#EXACTLY one number in a row
			prep=[]
			for i in range(1,10):
				prep.append(number(i,j,k))
			once(prep)


	for i in range(1,10,3):
		for j in range(1,10,3):
			for k in range (1,10):
				once([number(i+i1,j+j1,k) for (i1, j1) in itertools.product (range(3),repeat=2)]) #EXACTLY one number in a 3x3 block
	
	for j in range(1,10):
		prep=[]
		for k in range(1,10):
			prep.append(number(j,10-j,k))			#EXACTLY one number in a diagonal
		once(prep)
	pp=[]
	for a in range(1,10):
		for b in range(1,10):
			for k in range(1,10):
				if(a!=b):
					x=number(a,10-a,k)
					y=number(b,10-b,k)
					clauses.append([-x,-y])

									#EXACTLY one number in the other diagonal
	pp2=[]
	for a in range(1,10):
		for b in range(1,10):
			for k in range(1,10):
				if(a!=b):
					x=number(a,a,k)
					y=number(b,b,k)
					clauses.append([-x,-y])

	
	for i in range(0,9):
		for j in range(0,9):					#setting the already given prepostions in the unsolved matrix to true 
			if(sudoko[i][j]!='.'):
				clauses.append(number(i+1,j+1,int(sudoko[i][j])))


	with open('inputtemp1.txt','w') as f:
		f.write("p cnf {} {} \n".format(999,len(clauses)))
		for c in (clauses):
			c=str(c)
			for p in c:
				if (p!='[' and p!=']' and p!=','):		
					f.write("".join(p))
			f.write(" 0\n")


	os.system("minisat inputtemp1.txt outputtemp1.txt")
	with open('outputtemp1.txt','r') as f1:
		f2=''						#f1 contains the output file as a string
		for c in f1:	
			if(c=='UNSAT\n'):				#return 0 if unsatisfible
				return 0
			if(c=='SAT\n'):
				continue				
			else:
				for c1 in c:				#continuing if the current iteration gives satisfible output from minisat
					f2=f2+("".join(c1))
				f2=f2+("\n")
		flag=0
		final=''
		for i in range(0,len(f2)-3):
			if(f2[i]=='-'):
				flag=1
			if(f2[i]==' '):
				flag=0
			if(flag==0 and f2[i+1]!='-'):
				final=final+f2[i+1]
		fin2=[]
		sudoko1=[]
		for i in range(9):
			l=[]
			for j in range(9):
				l.append('.')
			sudoko1.append(l)
		for i in range(0,len(final)-2,4):
			fin2.append(int(final[i])*100+int(final[i+1])*10+int(final[i+2]))
		for i in fin2:
			first=int((str(i))[0])					
			second=int((str(i))[1])				#getting the position from hte first two digits
			third=int((str(i))[2])				# and the number to be filled in from the last digit of the preposition
			sudoko1[first-1][second-1]=third			
		return sudoko1				#returning the solved sudoko if solution exists

	
def numsol(sudoko):					#a function to retun the number of solution of the aruguement sudoko
	solved=solution(sudoko)
	neg=[]
	for i in range(9):
		for j in range(9):
			if (sudoko[i][j]=='.'):
				neg.append(-1*((i+1)*100+(j+1)*10+solved[i][j]))
	clauses=[]
	def number(i,j,k):
		 return 100*i+10*j+k
	def once(prep):
		clauses.append([l for l in prep])
		for p in itertools.combinations(prep,2):
			clauses.append([-l for l in p])
	for i in range(1,10):
		for j in range(1,10):
			prep=[]						#EXACTLY one number in a cell
			for k in range(1,10):
				prep.append(number(i,j,k))
			once(prep)
	
	for i in range(1,10):
		for k in range(1,10):					#EXACTLY one number in a column
			prep=[]
			for j in range(1,10):
				prep.append(number(i,j,k))
			once(prep)		

	for j in range(1,10):
		for k in range(1,10):
			prep=[]					#EXACTLY one number in a row
			for i in range(1,10):
				prep.append(number(i,j,k))
			once(prep)


	for i in range(1,10,3):
		for j in range(1,10,3):
			for k in range (1,10):
				once([number(i+i1,j+j1,k) for (i1, j1) in itertools.product (range(3),repeat=2)])	#EXACTLY one number in a 3x3 block
	for j in range(1,10):
		prep=[]
		for k in range(1,10):
			prep.append(number(j,10-j,k))		#EXACTLY one number in a diagonal
		once(prep)
	pp=[]
	for a in range(1,10):
		for b in range(1,10):
			for k in range(1,10):
				if(a!=b):
					x=number(a,10-a,k)
					y=number(b,10-b,k)			#EXACTLY one number in the other diagonal
					clauses.append([-x,-y])

	
	pp2=[]
	for a in range(1,10):
		for b in range(1,10):
			for k in range(1,10):
				if(a!=b):
					x=number(a,a,k)
					y=number(b,b,k)
					clauses.append([-x,-y])

	
	for i in range(0,9):
		for j in range(0,9):						
			if(sudoko[i][j]!='.'):						#setting the already given prepostions in the unsolved matrix to true 
				clauses.append(number(i+1,j+1,int(sudoko[i][j])))
	
	clauses.append(neg)
		
	if(clausesol(clauses)==1):	# 2 means multiple solution
		return 2		# 1 means single solution
	else:
		return 1

matrix=ransudo()
while(1):
	count=0
	start=0
	x=random.randint(0,8)			#choosing a random cell and removing its value 
	y=random.randint(0,8)
	while(matrix[x][y]=='.'):
		x=random.randint(0,8)
		y=random.randint(0,8)
	cell=matrix[x][y]
	matrix[x][y]='.'
	if(numsol(matrix)==2):			#if multiple solutions exits then fill in the removed number and continue the process
		matrix[x][y]=cell
		continue
	else:					#if it has single solution check whether it is minimal
		for i in range(9):		#travese over whole matrix adn if it gives multiple solution on removing any one number then the sokution is not minimal;continue picking random numbers
			for j in range(9):
				if(matrix[i][j]!='.'):
					celltemp=matrix[i][j]
					matrix[i][j]='.'
					if(numsol(matrix)==1):
						matrix[i][j]=celltemp
						start=1
						break
					else:
						matrix[i][j]=celltemp						
						count=count+1						
						continue
				else:	
					count=count+1		
				if(start==1):			
					break
			if(start==1):
				break
	if(count==81):				#when either the cells are empty or when the cell is filled gives multiple solution on removing a number
		break

string=''		#a string which stores the finally generated minimal sudoko as a 1d array
for i in range(9):
	for j in range(9):
		if (matrix[i][j]=='.'):
			string=string+'.'
		else:
			string=string+str(matrix[i][j])
with open('solution.txt','w') as f:						#saving the final output matrix in the file solution.txt
			for i in range(0,81,9):
				f.write(string[i:i+9])
				f.write("\n")


					















