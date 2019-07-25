HOW TO RUN THE PROGRAM:

1) Install cython in terminal by the simple command <<sudo apt install cython>>
2) Write down a “compile.py” in the same folder as the file “170212_170278a2.py”	 as follows:
*********************************************************************

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
#from Cython.Build import cythonize
ext_modules = [
    Extension("mymodule1",  ["170212_170278a2.py "]),
#   ... all your modules that need be compiled ...
]
setup(
    name = 'My Program Name',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

*********************************************************************
3) Write down a “main.py” in the same folder as the file “170212_170278a2.py”	 as follows:

*********************************************************************

from logic import main    
main ()

*********************************************************************

4) Feed the clauses encoding in a file named ”input.txt”
5) Then run <<python3 compile.py build_ext --inplace>>
6) Run  <<python3>> in the terminal
7) Run <<import mymodule1>>
8) The output will be saved in the out.txt file   


HEURISTICS:	

1) Selecting a clause for decomposition
Sorting the clauses in the order of their first literal’s absolute value .e.g.
a. -111 122 132 0
222 0
111 0
SORTED clauses becomes:
-111 122 132 0
111 0
222 0
2) Algorithm to decompose clauses
Picking the first literal of the first clause of the input list and making it false and then evaluating the semantic tableau recursively if solution array has a contradiction finally then negative of first literal is taken true and again same recursive calls are made to find the satisfiable answer 
IF there is again a contradiction then print UNSAT as for no valuation of first literal the semantic tableau does not close
3) Unit propagation 
Take a literal P and say it has valuation true then 
a) removing all the clauses that contain that literal P
b) removing just the literal from the clauses where the valuation of the literal is false i.e. -P


