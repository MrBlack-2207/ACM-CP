class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            res += (n % 2) * (2 ** i)
            n = n>>1
        return res

'''Approach:
Iterated through the bits of the number from the end to the start.
res is initialised to 0.
The modulus operator with 2 will extract the last digit of the number.
the last digit is then multiplied with 2 raised to the power of i , which will give us the correct position of the digit when it is reversed.
The number is then right shifted by 1 to get the next digit.
We can also use the // operator to shift the number to the right by 1.
But using bitwise shift operator is faster cause it uses only one register in the CPU whereas arithmetic operators use multiple registers.'''