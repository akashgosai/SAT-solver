# HOW TO RUN THE PROGRAM: 

1) Install cython in terminal by the simple command sudo apt install cython  
2) Write down a “compile.py” in the same folder as the file “170212_170278a2.py”	 as follows: 
*********************************************************************

        from distutils.core import setup  <br />
        from distutils.extension import Extension  <br />
        from Cython.Distutils import build_ext  <br />
        #from Cython.Build import cythonize  <br />
        ext_modules = [ 
            Extension("mymodule1",  ["170212_170278a2.py "]), 
           ... all your modules that need be compiled ... 
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
5) Then run python3 compile.py build_ext --inplace
6) Run  python3 in the terminal
7) Run import mymodule1
8) The output will be saved in the out.txt file  
