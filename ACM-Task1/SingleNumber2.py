class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones , twos = 0 , 0
        for num in nums:
            ones = (num^ones) & ~twos
            twos = (num^twos) & ~ones
        return ones

#Approach :
#Initial thought was to use a frequency array to count the frequency of each number and then return the number with frequence 1.But that would take O(n) space complexity.
#There was also a thought to sort the array and then check for the number which was not repeated but that would take O(nlogn) time complexity.
#After alot of googling, I found this approach using XOR operator which is efficient in both time and space.
#we create two variables namely ones and twos, and then we iterate through the array. "Ones" will store the number which occured once and "twos" will store the number which occured twice.
#ones = (num^ones) & ~twos
#twos = (num^twos) & ~ones
#the second time a number occurs , it will cancel itself in ones and appear in twice.
#the third time a number occurs , it clears itself from the "twos" as well.
#so the number which is left in "ones" is the number which has occured only once.
#and the number which is left in "twos" is the number which has occured twice.
#but the question specifies that there is only one number which occurs once. So, we return the number left in "ones".(without caring about the "twos")