def twoStacks(maxSum, a, b):
    n, m = len(a), len(b)
    sum_a = 0
    sum_b = 0
    count = 0
    
    # Remove from stack a as much as possible without exceeding maxSum
    i = 0
    while i < n and sum_a + a[i] <= maxSum:
        sum_a += a[i]
        i += 1
        count += 1
    
    # Now try removing from stack b without exceeding maxSum
    max_count = count
    j = 0
    while j < m:
        sum_b += b[j]
        j += 1
        count += 1
        
        # If the total sum exceeds maxSum, stop and adjust by removing from stack a
        while sum_a + sum_b > maxSum and i > 0:
            i -= 1
            sum_a -= a[i]
            count -= 1
        
        max_count = max(max_count, count)
    
    return max_count

# Read input and process multiple test cases
if __name__ == "__main__":
    t = int(input())  # number of test cases
    for _ in range(t):
        n, m, maxSum = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(twoStacks(maxSum, a, b))