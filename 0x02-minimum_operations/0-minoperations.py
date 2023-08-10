#!/usr/bin/python3
"""
Below is the module for minimum operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to obtain n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 0:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations

# Test cases
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

