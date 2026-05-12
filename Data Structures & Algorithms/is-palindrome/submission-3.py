class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # # a-z
        # lower_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        # # A-Z
        # upper_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        # # 0-9
        # digits_list = [chr(i) for i in range(ord('0'), ord('9') + 1)]

        palin = ""
        # for char in s:
        #     if (char in lower_list or char in digits_list):
        #         palin += char
        #     elif(char in upper_list):
        #         lower = chr(ord('a') + (ord(char) - ord('A')))
        #         palin += lower

        for char in s:
            if (self.alphaNum(char)):
                palin += char.lower()

        i,j = 0, len(palin)-1
        while i<j:
            if (palin[i]!=palin[j]):
                return False
            i+=1
            j-=1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        