# HCF and GCD both are same 
# Going to find the greatest common number which divides the given number 

# non-recursive method

def hcf(x, y):

    minimum = min(x, y)

    if x%minimum == 0 and y%minimum == 0:
        return minimum
    
    for i in range(minimum//2, 1, -1):
        if x%i == 0 and y%i == 0:
            return i
    
    return 1

print('HCF', hcf(12, 15))


# naive approach

def naive_hcf(x, y):

    result = min(x, y)

    while result:
        if x%result == 0 and y%result == 0:
            return result
        result -= 1
    return result

print('Naive HCF', naive_hcf(12, 15))


# recursive approach for HCF or GCD

def recursive_hcf(x, y):

    if x == 0:
        return y
    
    if y == 0:
        return x
    
    if x == y:
        return x
    
    if x > y:
        return recursive_hcf(x%y, y)
    return recursive_hcf(x, y%x)

print('Recursive HCF', recursive_hcf(12, 15))


# optimization using division

def optimal_hcf(x, y):

    if y == 0:
        return x
    return optimal_hcf(y, x%y)

print('Optimization using division', optimal_hcf(12, 15))
