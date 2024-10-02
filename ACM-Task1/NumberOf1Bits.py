class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            if n&1==1:
                count+=1
            n = n>>1
        return count
    
'''Approach:
ran a loop for 32 times cause the number is 32 bit.
and everytime , checked if the last bit of the number is 1 or not.
incremented the count if yes, and then right shifted the number by 1.(//2)
returning the count at the end.'''