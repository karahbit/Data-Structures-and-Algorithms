# Efficient Approach: Convert int to binary string
# Keep dividing the number by 2 until it is greater than or equal to 1. Add the remainder to the string at each step.
# TC = O(logn)
# SC = O(1)
def hamming_weight(n):
    ans = 0

    while n >= 1:
        ans += n % 2
        n //= 2

    return ans


print(hamming_weight(7))


# Optimal Approach: Bit Manipulation
# If we turn off every rightmost 1-bit (x & (x-1)), at some point the number will be zero. Increase the count by 1 at each step.
# TC = O(n) = O(1) since # of bits are capped at 32
# SC = O(1)
def hamming_weight(n):
    ans = 0

    while n:
        n &= (n-1)
        ans += 1

    return ans


print(hamming_weight(7))
