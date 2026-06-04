# Data Structures and Methods for HPC

# Exercise 1 - PyTest with the Julia Set Code

As part of this exercise, we ask you to experiment with the pytest framework used for unit testing and the Julia set code.

In the Julia Set Code, we have a simple assertion to check the correctness of the code.

    - This sum is expected for a $$ {1000}^2 $$ grid with $$ 300 $$ iterations
    -It It ensures that our code evolves exactly as we'd intended to assert **sum(output) == 33219980**

In this exercise, we'd like to ask you to develop a test unit to check this assertion using the pytest framework.

# **Task 1.1**

Implement a separate code to test the assertion above using the pytest framework.

# **Task 1.2**

How would you implement the unit test with the possibility of having a different number of iterations and grid points? Implementation is optional.

#*****************************************************************#

# Exercise 2 - Python DGEMM Benchmark Operation

The **BLAS** library is a critical library for HPC. **DGEMM** is an important computational kernel, part of the **BLAS** library, solving the problem **$$ C = C + A * B $$**, where **A, B and C** are matrices of size **NxN**.  In this exercise, we will use matrices with double precision values (that is why we have <ins>D in DGEMM</ins>). The three matrices can be initialized as you think it is convenient, e.g., fixed or random values.

The <ins>pseudo-code</ins> in <ins>C-style (no Python)</ins> for the DGEMM is the following:


    $ // Multiplying first and second matrices and storing it in result
    $    for (int i = 0; i < N; ++i) {
    $        for (int j = 0; j < N; ++j) {
    $            for (int k = 0; k < N; ++k) {
    $                C[i][j] = C[i][j] + A[i][k] * B[k][j];
    $            }
    $        }
    $    }


You will need to implement this operation in Python using different approaches. We will use this DGEMM benchmark to calculate the computational performance of the system you are using.

The goal of this exercise is to implement, profile, analyze, and compare the performance of different Python DGEMM implementations with lists, arrays, and NumPy

# **Task 2.1**

Implement the DGEMM with matrices as NumPy array

# **Task 2.2**

Using pytest develop a unit test for checking the correctness of your implementations.

# **Task 2.3** 

Measure the execution time for each approach varying the matrix size. Report the average and error (std. deviation, min/max, or interval of confidence). 

# **Task 2.4** 

Using the timing information and the number of operations for the DGEMM, calculate the FLOPS/s. 

# **Task 2.5**

Compare the performance results with the numpy matmul operation (that uses a BLAS library). 


#*****************************************************************#


# Exercise 3 - Experiment with the Python Debugger

As part of this exercise, we ask you to complete an online tutorial on the Python pdb debugger. Follow the instructions at https://github.com/spiside/pdb-tutorial.

# **Task 3.1**

Reflection


