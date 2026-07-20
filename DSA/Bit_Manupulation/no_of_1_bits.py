# 191. Number of 1 Bits

class Solution:     # no_of_iteration =  no of bits present
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        while n:
            if n&1:
                set_bits += 1
            n = n>>1
        return set_bits
    

class Solution:     # no_of_iteration = no_of set bits present
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n&(n-1)     # Brian Kernighan's Algorithm
        return count