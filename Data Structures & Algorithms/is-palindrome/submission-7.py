class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        # while(i<j):
        #     if not s[i].isalnum():
        #         i+=1
        #         continue
        #     if not s[j].isalnum():
        #         j-=1
        #         continue
        #     if s[i].lower()!=s[j].lower():
        #         return False
        #     i+=1
        #     j-=1
        # return True
        while True:
            if i == j or i > j:
                return True
            should_continue = False
            if not s[j].isalnum() or s[j] == ' ':
                j -=1
                should_continue = True
            if not s[i].isalnum() or s[i] == ' ':
                i +=1
                should_continue = True
            if should_continue:
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1