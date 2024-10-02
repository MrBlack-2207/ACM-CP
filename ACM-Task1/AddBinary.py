class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        a , b = a[::-1] , b[::-1]
        carry = 0
        for i in range(max(len(a),len(b))):
            digit1 = ord(a[i])-ord('0') if i<len(a) else 0
            digit2 = ord(b[i])-ord('0') if i<len(b) else 0
            total = digit1+digit2+carry
            char = str(total%2)
            ans = char + ans
            carry = total//2
        
        if carry:
            return "1" +ans
        else:
            return ans

'''Approach:
Initially thought of iterating through the strings from the end but then realised reversing the strings would be better cause we have to add zeroes to the smaller string.
Initialised the carry to zero and then iterated through the reversed strings.
Converted the characters to integers and added them along with the carry.
the "totalsum" is the sum of the two digits and the carry.
The character is the remainder of the total sum divided by 2 cause that will give us the right binary digit.
Handled an edge case where we get carry in the last iteration.'''