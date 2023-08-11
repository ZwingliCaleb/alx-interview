#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to get 'n' H characters in a text file.

    :param n: The desired number of H characters.
    :return: The minimum number of operations required.
             Returns 0 if achieving 'n' is impossible.
    """

    if n <= 0:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')  # Initialize with a large value
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j - 1)
                dp[i] = min(dp[i], dp[i // j] + j - 1)

    return dp[n]

# Example usage
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
