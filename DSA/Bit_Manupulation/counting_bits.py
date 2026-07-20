# 338. Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = []
        for i in range(n+1):
            set_bits = 0
            while i:
                if i&1:
                    set_bits += 1
                i = i>>1
            answer.append(set_bits)
        return answer