import mlpux
import math

@mlpux.Demo()
def sum_combinations(n):
    sum = 0
    for k in range(n+1):
        sum += math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    return sum