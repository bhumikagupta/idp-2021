class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start, i = 0, 0
        maxi = 0
        
        while i < len(s) :
            if s[i] not in seen :
                maxi = max(maxi, i-start+1)
                seen.add(s[i])  
                i+=1 
            else :
                start += 1
                seen = set(s[start]) 
                i= start+1  
                
                
        return maxi
