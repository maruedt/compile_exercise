# exercise-compiler
exercise-compiler.py compiles Jupyter exercises into output files

exercise-compiler.py accepts the path to a jupyter notebook based exercise. It converts the exercise in 4 outputs:
1. HTML file without cells tagged as 'solution'
2. Jupyter Notebook without cells tagged as 'solution'
3. HTML file with all cells. 'solution' is added to the file name.
4. Jupyter Notebook with all cells. 'solution' is added to the file name.

The files are stored in a subdirectory called output. If the files already exist, they are overwritten.