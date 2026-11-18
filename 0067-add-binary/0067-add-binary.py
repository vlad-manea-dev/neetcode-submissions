"""
a = "1010", 
b = "1011"

        10101

a = "10111", 
b = "10111"

        11110
a = 11
b = 01

    100

add final index from both + carry
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b):
            if len(a) > len(b):
                b = b.zfill(len(a))
            else:
                a = a.zfill(len(b))
        
        carry = 0
        binary = []
        for i in range(len(a) - 1, - 1, -1):
            curSum = int(a[i]) + int(b[i]) + carry
            bit = curSum % 2
            carry = curSum // 2
            binary.append(str(bit))
        if carry == 1:
            binary.append(str(1))
        return "".join(binary[:: -1])
            
