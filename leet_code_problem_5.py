class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_substring = ''

        if len(s) > 1:

            if len(s) == 2:
                if s == s[::-1]:
                    return s
                else:
                    return s[0]

            for i in range(len(s)):

                for j in range(len(s)-1, i, -1):

                    
                    first_part = s[i:j+1]
                    rev_s = first_part[::-1]

                    if first_part == rev_s:
                        if len(longest_substring) < len(first_part):
                            longest_substring = first_part

                 
            return longest_substring if longest_substring != '' else s[0]        

        else:
            return s
        
