class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedString = ''.join(char for char in s if char.isalnum())
        cleanedString = cleanedString.lower()
        L,R = 0, len(cleanedString) - 1

        while L <= R: 
            if cleanedString[L] == cleanedString[R]:
                L += 1 
                R -= 1
            else: 
                return False
        return True