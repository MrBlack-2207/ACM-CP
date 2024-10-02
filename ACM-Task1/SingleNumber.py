class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for i in nums:
            single = single^i
        return single
    
#Approach :
#First thought was to sort the array and then check for the number which is not repeated but that would take O(nlogn) time complexity.
#So, I used the XOR operator to solve this problem. XOR of a number with itself is 0. So, if we XOR all the numbers in the array, the repeated numbers will cancel each other out and we will be left with the single number.
#Time complexity : O(n)
#Space complexity : O(1)
#We can also do this with hashset , by noting down the frequency of each number and then checking for the number with frequency 1. But that would take O(n) space complexity.