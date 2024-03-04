# Atam_Ex3_Tests
How To Run:
* On a linux Machine/wsl/linux VM:
1. Go into "part1" directory:
```cd part1```

2. Paste your students_code.S script into "part1" directory
```cp <your_students_code.S_file_path> .```

3. Make sure your current working directory is "part1" and you have the following files there:
- aux_hw3.o
- better_basic_test.sh
- better_test1.c
- python_test.py
- students_code.S

# Run Command:
```python3 python_test.py 10```

* Change the number '10' with the number of tests YOU want to run.

# Prerequisites
* Make sure you have python3 installed and you run this code on a UNIX machine.

# How do they work?
- The tests generate 2 matrices each time (given generated_num times) A: mxn, B: pxq.

- There is a 30% chance of generating a "bad" pair of matrices that are incompatible for matrix multiplication in terms of their dimensions (n != p).

- The tests use an improved version of the given test1.c and basic_test.sh
* test1.c: I have changed so that it will get input from the user instead of defining magic numbers and constants for it's variables, and I added functionality to handle the case when the matrices are incompatible and the assembly script needs to return 0 (according to my guess of how they'll do it).
* basic_test.sh: I modified to add colors, and in the case of a difference between actual output and expected output, save the output of your assembly script (instead of deleting) and displaying the difference using cat command (you can change to other difference showing commands if you'd like).

- The tests will create an "outputs" directory on the directory you ran them on. It will contain the actual outputs vs expected outputs of tests that have failed.
