import numpy as np
from array import array
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from prettytable import PrettyTable


#numpy
def dgemm_numpy(A, B):
    v = np.dot(A, B)
    return v

#list 
def dgemm_list(A, B, n):
    C = [[0.0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

#array
def dgemm_array(A, B, n):
    C = [array('d', [0.0] * n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C



# measure execution time and FLOPS
def benchmark_dgemm(n, num_t = 5):
    results = {"dgemm_numpy": [], "dgemm_list": [], "dgemm_array": [] }

    for _ in range(num_t):
        Anp = np.random.random((n, n)).astype(np.float64)
        Bnp = np.random.random((n, n)).astype(np.float64)


        #numpy dgemm
        start = timer()
        _ = dgemm_numpy(Anp, Bnp)
        results["dgemm_numpy"].append(timer() - start)


        #list dgemm
        A_list = Anp.tolist()
        B_list = Bnp.tolist()
        start = timer()
        _ = dgemm_list(A_list, B_list, n)
        results["dgemm_list"].append(timer() - start)



        #Array dgemm
        Aarray = [array('d', row) for row in A_list]
        Barray = [array('d', row) for row in B_list]
        start = timer()
        _ = dgemm_array(Aarray, Barray, n)
        results["dgemm_array"].append(timer() - start)



    #compute statistics
    summary = {}
    for method in results:
        times = np.array(results[method])
        avg = times.mean()
        min_time = times.min()
        max_time = times.max()
        std_dev = times.std()
        flops = (2 * n**3) / avg



        summary[method] = {
            "avg_time": avg,
            "min_time": min_time,
            "max_time": max_time,
            "std_dev": std_dev,
            "flops": flops
        }

    return summary
    



if __name__ == "__main__":
    sizes = [10, 100, 1000]
    results = {size: benchmark_dgemm(size) for size in sizes}


    table = PrettyTable(["Size", "Method", "Avg Time ", "Min Time", "Max Time", "Std Dev", "FLOPS"])
    for n in sizes:
        for method in results[n]:
            data = results[n][method]
            table.add_row([
                n, method,
                f"{data['avg_time']:.6f}",
                f"{data['min_time']:.6f}",
                f"{data['max_time']:.6f}",
                f"{data['std_dev']:.6f}",
                f"{data['flops']:.6f}"
            ])

    print(table)


    
    









