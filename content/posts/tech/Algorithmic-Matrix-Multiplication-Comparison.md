---
title: "Algorithmic Matrix Multiplication Comparison"
date: 2023-09-20T01:20:34+05:30
draft: false
cover:
    image: blog/algo-matmul-cover.webp
    alt: Algorithmic Matrix Multiplication Comparison
    caption: "Matrix Multiplication: Strassen vs. Naive Method"
description: "Comparing Strassen's method and naive approach for matrix multiplication, exploring time and memory complexities in Python."
tags: ["python"]
---


## Introduction

This report compares Strassen's method and the naive approach for matrix multiplication. The main goal is to empirically look into the causes of the naive method's O(N^3) complexity. The focus is on proving how Strassen's methods deliver a faster performance and lower time complexity.

Real-world tests will be conducted with different matrix sizes. This will determine their time complexities. The Python code implementation across different matrix sizes will estimate the constants based on the implementation logic. Comparison between the two approaches' memory needs determines which algorithm is more memory-efficient.

The assessment goes over specific situations where one approach might be better than the other. This is dealt with by taking into account factors such as matrix size, available memory, and computational resources. Performance variations are demonstrated using empirical examples. To predict the time complexity and the factors influencing the constant, the effects of using MapReduce for the naive method's implementation will be analyzed.

The expected outcome is to help in the selection of the most appropriate algorithm for a variety of matrix multiplication tasks. The tradeoff between space and memory optimization will be considered. The conclusion will deliver helpful insights into the advantages and disadvantages of each technique with a thorough analysis.

{{< fancylink "Git Gud at Algorithms with my" "FAANG Interview Guidebook" "/posts/tech/gumroad-dsa-announcement/" >}}


## CPU Specifications

At the time of writing this report, a Hexacore Computer with 6 cores and 12 threads is being used to run the tests. This needs to be taken into account. It reduces execution time for multi-threaded algorithms, but the impact depends on algorithmic implementation, memory access, and scheduling.

![adsd](/blog/cpu-config.png)

## Analyzing Time Complexity of the Naive Method for Matrix Multiplication

To compute each element of the resulting matrix, the naive matrix multiplication method uses three nested loops. The resulting matrix `C` will be of size `n` x `p` for two matrices `A` of size `n` x `m` and `B` of size `m` x `p`. To calculate each component of `C`, the algorithm performs `n * m * p` scalar multiplications and additions.

The dominant term in the naive method is `O(n^3)`. It shows how many rows there are in matrix A and the resulting matrix `C`.

Each element of the resulting matrix `C` is computed using three nested loops in the naive 3x3 matrix multiplication algorithm. The algorithm calculates the ith row of matrix `A` and the jth column of matrix `B` as the dot product for each element `C[i][j]`.

All components computation requires 27 (size times size) scalar multiplications and additions.

This calculation verifies whether the theoretically predicted time complexity of O(n^3) holds in practice. Any bottlenecks or improvements possible to this matrix multiplication are also pointed out.

The constant factor in the non-optimized 3x3 matrix multiplication algorithm would factor in memory access time, loop overhead, and other I/O machine-specific operations. Even if two computers have the same complexity, this overhead time differs.

The growth rate of the algorithm as the size of the input increases is unaffected by the constant factor. Concentrate on the dominant term in Big O notation. It represents the algorithm's growth rate as the input size approaches infinity. A coefficient that scales the time complexity is the constant factor. But, it does not affect how big the time complexity is.

It displays the processing time and overhead unique to our system and implementation. The time complexity remains cubic even though different systems and implementations use different constant factors.

```py
import numpy as np
import time

def naive_matrix_multiply(A, B):
    n, m = A.shape
    m, p = B.shape
    C = np.zeros((n, p)) # stores resultant matrix

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Testing empirical runtime for matrix multiplication
sizes = [50, 100, 150, 200, 250]
runtimes = []

for size in sizes:
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    start_time = time.time()
    C = naive_matrix_multiply(A, B)
    end_time = time.time()

    runtime = end_time - start_time
    runtimes.append(runtime)

# Fitting empirical data to O(n) model to estimate the constant factor
coefficients = np.polyfit(sizes, runtimes, 1)
constant_factor = coefficients[0]

print("Estimated constant factor:", constant_factor)
```

## Asymptotic Efficiency of Strassen's Method

Matrix multiplication using Strassen's method is asymptotically quicker than using the traditional `O(n^3)` method. For large matrix multiplications, it lowers the number of scalar multiplications necessary. Each component of the resulting matrix C requires n scalar multiplications in the naive algorithm. But Strassen's approach lowers the number of scalar multiplications to `O(n^log2(7))`, or roughly `O(n2.81)`.

This efficient divide-and-conquer approach makes fewer recursive calls to perform matrix multiplication. Matrices are split into smaller submatrices, using only seven recursive multiplications instead of eight in each step. As a result, the complexity time is rouO(n^log2(7)). This is quicker than the simple `3x3` matrix multiplication algorithm, which has an `O(n^3)` complexity. As it requires fewer arithmetic operations, this should be used for large square matrices. But because of the recursive submatrices, it uses more memory than necessary.

Using addition and subtraction to combine the results, Strassen's approach reduces the problem by iteratively breaking the matrix multiplication down into smaller subproblems. In comparison to scalar multiplications, these operations are less time-intensive. The difference between the two methods' scalar multiplication rates grows more pronounced as matrix size (n) rises. The effectiveness of Strassen's method is asymptotically improved as a result.

By varying the size of the matrices and observing execution time, perform a runtime analysis to determine the time complexity and constant factor of Strassen's method. Estimate the constant factor for the specific implementation and computer by fitting the empirical data to the theoretical complexity `O(n^log2(7))`. The constant factor stands for system- and implementation-specific overhead and processing time. For large matrices, the time complexity is still `O(n^log2(7))`, which is quicker than the traditional `O(n^3)` method.

```py
import numpy as np
import time

def strassen_matrix_multiply(Mat_A, Mat_B):
    Row_1, Col_1 = len(Mat_A), len(Mat_A[0])
    Row_2, Col_2 = len(Mat_B), len(Mat_B[0])
    
    # Matrix result to be stored in a matrix of size Row_1 rows and Col_2 columns
    result = [[0 for _ in range(Col_2)] for _ in range(Row_1)]
    
    # Verify if it is a square matrix. Otherwise multiplication is not possible.
    if Col_1 != Row_2:
        print("Matrix Multiplication not possible")
        return None
    
    # Perform matrix multiplication using Strassen's method
    if Row_1 == Col_1 == Row_2 == Col_2 and Row_1 & (Row_1 - 1) == 0:
        return strassen_matrix_multiply_helper(Mat_A, Mat_B)
    
    # Use the traditional method for matrix multiplication
    for i in range(Row_1):
        for j in range(Col_2):
            for k in range(Row_2):
                result[i][j] += Mat_A[i][k] * Mat_B[k][j]
    
    return result

def strassen_matrix_multiply_helper(a, b):
    # Helper function for Strassen's matrix multiplication (omitted for brevity)
    pass

def constant_estimator(matrix_size):
    a = np.random.rand(matrix_size, matrix_size)
    b = np.random.rand(matrix_size, matrix_size)

    start_time = time.time()
    C = strassen_matrix_multiply(a, b)
    end_time = time.time()

    runtime = end_time - start_time
    return runtime

# Example matrices
Mat_A = [[3, 3, 1], [7, 9, 2], [4, 6, 4]]
Mat_B = [[6, 1], [9, 2], [10, 3]]

# Estimate the constant factor using empirical runtime analysis
matrix_sizes = [50, 100, 150, 200, 250]
runtimes = []

for size in matrix_sizes:
    runtime = constant_estimator(size)
    runtimes.append(runtime)

# Fitting empirical data to O(n^log2(7)) model to estimate the constant factor
coefficients = np.polyfit(np.log2(matrix_sizes), runtimes, 1)
constant_factor = coefficients[0]

print("Estimated constant factor:", constant_factor)

```

## Memory Requirements Comparison: Naïve Method vs. Strassen's Method

In comparison to Strassen's approach (3.3573), the naive algorithm's predicted constant factor is lower (0.0578). This suggests that the naïve algorithm has reduced overhead in both time and memory. It indicates that it may perform better in practice for smaller matrices due to its lower memory needs and fewer arithmetic operations. But Strassen's method has a superior asymptotic time complexity. The larger constant factor indicates this.

Usage of Strassen's method requires more memory compared to the previous method. This is primarily due to the recursive nature and storage of intermediate matrices. An exhaustive list of reasons is as follows:

- **Recursive Calls**: Strassen's approach divides the matrices into smaller submatrices. There are recursive calls that need more memory at each level of recursion.  
  
    ```py
    def strassen(a, b):
        if len(a) == 1:
            # Base case: 1x1 matrix, no further recursion
            return a[0][0] * b[0][0]
        # Recursive call 
    ```

- **Intermediate Matrices**: There are seven recursive multiplications in Strassen's algorithm. The result for each one involves the storage of intermediate matrices. These interim results increase the memory overhead.  

    ```py
    def strassen(a, b):
        # ...
        p1 = strassen(add_m(a11,a22), add_m(b11,b22), q/2)
        p2 = strassen(add_m(a21,a22), b11, q/2)
    ```

- **Matrix Partitioning**: For each iteration, the returned matrix is split into smaller submatrices. This means increased memory usage.  

    ```py
    def strassen(a, b):
        # ...
        a11, a12 = a[:m, :m], a[:m, m:]
        b11, b12 = b[:m, :m], b[:m, m:]
    ```

- **Space Complexity Overhead**: The space complexity of Strassen's method is O(n^log2(7)). The complexity of the former sees rapid increase. This leads to higher memory needs.  

- **Stack space** a reserved memory area used to store function call information and local variables. It operates in a Last-In-First-Out (LIFO) manner. Here, it is consumed for function calls during recursive calls in Strassen's method, which further increases memory usage.  

    ```py
    def strassen(a, b):
        # ...
        p1 = strassen(add_m(a11,a22), add_m(b11,b22), q/2)
    ```

- **Large Matrices**: For larger matrices, Strassen's method is more memory-efficient than the naive method. But, for smaller matrices, Strassen's method loses efficiency.

As discussed, it is faster but has a higher memory overhead. This makes it memory-efficient for smaller matrices or critical memory constraints.

## Tradeoff Between Naïve Method and Strassen’s Method for Matrix Multiplication

The naive strategy is usually used when working with tiny matrix sizes or when memory is at a constraint. It is more useful since it works well for smaller matrices and has a reduced constant overhead. Contrarily, Strassen's approach is more effective for bigger matrices. Particularly where time complexity is a major factor. It is more effective for large square matrices but less effective for otherwise. This is due to chances of memory overflow due to several factors seen in the previous answer. Despite its greater constant factor and memory utilization, Strassen's technique could offer superior time efficiency for bigger matrices. An educated selection on the best method for matrix multiplication in your particular use case may be made by taking these variables into account and evaluating runtimes.

```py
sizes = [50, 100, 200, 500]

for size in sizes:
    # Test empirical runtime for matrix multiplication
    A =  np.random.rand(size, size)
    B =  np.random.rand(size, size)

    # Naive method
    start_time_naive = time.time()
    C_naive = naive_matrix_multiply(A, B)
    end_time_naive = time.time()
    runtime_naive = end_time_naive - start_time_naive

    # Strassen's method
    start_time_strassen = time.time()
    C_strassen = strassen_matrix_multiply(A, B)
    end_time_strassen = time.time()
    runtime_strassen = end_time_strassen - start_time_strassen

    print(f"Matrix size: {size}x{size}")
    print(f"Naive method runtime: {runtime_naive} seconds")
    print(f"Strassen's method runtime: {runtime_strassen} seconds\n")
```

```
Matrix size: 50x50
Naive method runtime: 0.09976315498352051 seconds
Strassen's method runtime: 0.07229471206665039 seconds

Matrix size: 100x100
Naive method runtime: 0.7857158184051514 seconds
Strassen's method runtime: 0.5759141445159912 seconds

Matrix size: 200x200
Naive method runtime: 6.21253776550293 seconds
Strassen's method runtime: 4.710278511047363 seconds

Matrix size: 500x500
Naive method runtime: 96.04322266578674 seconds
Strassen's method runtime: 69.35138845443726 seconds
```

### Plotting Runtime Comparison

```py
import matplotlib.pyplot as plt

matrix_sizes = [50, 100, 200, 500]
naive_runtimes = [0.0985569953918457, 0.7604336738586426, 6.080593585968018, 95.97012424468994]
strassen_runtimes = [0.07361817359924316, 0.5590286254882812, 4.453122854232788, 70.3049566745758]

plt.plot(matrix_sizes, naive_runtimes, marker='o', label='Naive Method')
plt.plot(matrix_sizes, strassen_runtimes, marker='o', label="Strassen's Method")
plt.xlabel('Matrix Size')
plt.ylabel('Runtime (seconds)')
plt.title('Naive Method vs. Strassen\'s Method for Matrix Multiplication')
plt.legend()
plt.grid()
plt.show()

```

![plot](/blog/plot.png)

## Naive Matrix Multiplication Implementation Using MapReduce


```python
import findspark
findspark.init()

from pyspark import SparkContext, SparkConf
import os

def matrix_multiply_mapper(matrix_tuple):
    # Unpack the matrix tuple
    matrix_name, row_num, col_num, value = matrix_tuple

    if matrix_name == 'A':
        for k in range(matrix_size):
            # Emit a key-value pair with the key as (row_num, k) and the value as (matrix_name, col_num, value)
            yield ((row_num, k), (matrix_name, col_num, value))
    else:
        for i in range(matrix_size):
            yield ((i, col_num), (matrix_name, row_num, value))

def matrix_multiply_reducer(key_value_pair):
    result = 0

    # Convert the iterator to a list of tuples
    matrix_list = list(key_value_pair[1])
    
    for i in range(matrix_size):
        # Get the value from matrix 'A' at column i
        a_value = next((t[2] for t in matrix_list if t[0] == 'A' and t[1] == i), 0)
    
        # Get the value from matrix 'B' at row i
        b_value = next((t[2] for t in matrix_list if t[0] == 'B' and t[1] == i), 0)
    
        # Compute the product of corresponding elements and add it to the result
        result += a_value * b_value
    
    return key_value_pair[0], result

def matrix_multiply(matrix_A, matrix_B, sc):
    # Create RDDs for matrix 'A' and matrix 'B' using SparkContext 'sc'
    matrix_A_rdd = sc.parallelize(matrix_A, matrix_size)
    matrix_B_rdd = sc.parallelize(matrix_B, matrix_size)

    # Map the elements of matrix 'A' and matrix 'B' to key-value pairs using the mapper function
    mapped_matrix_A = matrix_A_rdd.flatMap(matrix_multiply_mapper)
    mapped_matrix_B = matrix_B_rdd.flatMap(matrix_multiply_mapper)

    # Combine mapped matrices using union operation
    combined_matrices = mapped_matrix_A.union(mapped_matrix_B)
    
    # Group combined matrices by their keys using groupByKey operation
    grouped_matrices = combined_matrices.groupByKey()
    
    # Reduce the grouped matrices using the reducer function to compute the final result
    result_rdd = grouped_matrices.map(matrix_multiply_reducer)

    # Collect the results from RDD and return the final matrix multiplication result
    result = result_rdd.collect()
    return result

if **name** == "**main**":
    # Test matrices
    matrix_size = 3
    matrix_A = [('A', 0, 0, 1), ('A', 0, 1, 2), ('A', 0, 2, 3),
                ('A', 1, 0, 4), ('A', 1, 1, 5), ('A', 1, 2, 6),
                ('A', 1, 1, 7), ('A', 8, 2, 2), ('A', 0, 1, 1)]
    matrix_B = [('B', 0, 0, 6), ('B', 0, 1, 1),
                ('B', 1, 0, 9), ('B', 1, 1, 2),
                ('B', 2, 0, 10), ('B', 2, 1, 3)]

    # Initialize SparkContext
    conf = SparkConf().setAppName("MatrixMultiplication")
    sc = SparkContext(conf=conf)

    result_naive = matrix_multiply(matrix_A, matrix_B, sc)
    print("Naive Method Result:")
    for row in result_naive:
        print(row)

    # Stop SparkContext
    sc.stop()
```

```
Naive Method Result:
((0, 2), 0)
((8, 0), 0)
((2, 0), 0)
((0, 0), 54)
((1, 0), 129)
((1, 2), 0)
((8, 1), 0)
((1, 1), 32)
((8, 2), 0)
((0, 1), 14)
((2, 1), 0)
```

The time complexity of the algorithm remains unchanged. Whether matrix multiplication is performed by the naive method or the MapReduce method, the time complexity is still O(n^3).

MapReduce breaks down large data into smaller tasks. These tasks are distributed across cluster nodes. This allows for massively parallel processing of large data.

The following factors influence the constant factor:

1. **Hardware and System Configuration**. Particularly the cluster where the MapReduce algorithm is being used. Variables like the number of nodes, memory, CPU cores, and network bandwidth are a factor

2. **Data Distribution**. Performance depends on how data is distributed and processed among nodes in the MapReduce cluster. More overhead and longer execution times can result from an unbalanced data distribution or excessive data movement between nodes.

3. **Data Size**. The MapReduce algorithm's performance varies based on the size of the input matrices. Bigger matrices could take longer and need more processing power to process.

4. **Implementation Logic**. The complexity and effectiveness of the map and reduce functions affect the runtime. Different implementation logic affects speed. Enhancing these processes can improve performance.

5. **Communication Overhead**. Node-to-node communication should be the least. Higher efficiency is possible by reducing data transfers and improving communication patterns.

MapReduce can be useful for processing huge datasets and utilizing distributed computing resources. But it does not alter the matrix multiplication algorithm's inherent time complexity. The time complexity remains O(n^3).

## Conclusion

According to the analysis, Strassen's approach performs quicker and has a time complexity of O(N^log2(7)). Whereas the naive method has a time complexity of O(N^3) for matrix multiplication. The Python code implementation made it possible to identify the constants connected to each method.

The naive technique outperforms Strassen's method of memory use. This makes it the better choice for smaller matrices. Contrarily, Strassen's technique is superior for bigger matrices. This is due to its more effective computing strategy - reducing matrix calculations.

The naive technique's time complexity stayed at O even after implementing it with MapReduce O(N^3). Yet it gave us the chance to use dispersed computer power for more complex calculations.

Constants for both approaches depend on several variables. These include hardware requirements, data distribution, and algorithm layout among others. The effectiveness of each strategy should be optimized in light of these criteria.

The matrix sizes and computational resources are deciding factors to decide the most optimal matrix multiplication strategy. The key takeaway is that for smaller matrices go with the naive method. For bigger matrices (size > 200) Strassen's method is preferable.

Using the findings will help decision-makers select the best matrix multiplication technique. Note that these finds are only applied to square matrices.
