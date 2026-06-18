class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        list = [str.lower() for str in s if str.isalnum()]
        return list == list[::-1]