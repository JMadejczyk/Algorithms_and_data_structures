# Implement the Fibonacci sequence using both memoization and tabulation. Compare their performance for n = 50.

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def fib_tab(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


import time
n = 50
start_memo = time.time()
result_memo = fib_memo(n)
end_memo = time.time()
start_tab = time.time()
result_tab = fib_tab(n)
end_tab = time.time()
print(f"Fibonacci with Memoization for n={n}: {result_memo}, Time: {end_memo - start_memo:.6f} seconds")
print(f"Fibonacci with Tabulation for n={n}: {result_tab}, Time: {end_tab - start_tab:.6f} seconds")
# So tabulation is faster than memoization (at least for n = 50)