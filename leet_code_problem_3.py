class Solution(object):
   
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        current_substring = []

        max_reached_len = 0

        if s != None:
            
            for i in range(len(s)):
                # start the search from every letter

                current_letter = s[i]
                current_substring.append(current_letter)
                
                for j in range(i+1, len(s)):
                    # continue the search from the element next to the chosen one by index i

                    next_letter = s[j]
                    if next_letter not in current_substring:
                        current_substring.append(next_letter)

                    else:
                        current_len = len(current_substring)
                        if max_reached_len < current_len:
                            max_reached_len = current_len
                        current_substring = []
                        break

                current_len = len(current_substring)
                if max_reached_len < current_len:
                    max_reached_len = current_len
                current_substring = []



        return max_reached_len



                    
        
