import sys
sys.setrecursionlimit(3000)

def recursive_variance(values, index=0, sum_val=0, sum_sq=0, count=0):

    # Base condition
    if index == len(values):
        if count == 0:
            return 0
        mean = sum_val / count
        return (sum_sq / count) - (mean ** 2)

    return recursive_variance(
        values,
        index + 1,
        sum_val + values[index],
        sum_sq + values[index] ** 2,
        count + 1
    )