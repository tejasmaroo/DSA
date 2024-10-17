class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        # Hash maps to store the mapping between characters of s and t
        s_to_t = {}
        t_to_s = {}
        
        for c1, c2 in zip(s, t):
            # Check if there is an existing mapping from s to t
            if c1 in s_to_t:
                if s_to_t[c1] != c2:
                    return False
            else:
                s_to_t[c1] = c2
            
            # Check if there is an existing mapping from t to s
            if c2 in t_to_s:
                if t_to_s[c2] != c1:
                    return False
            else:
                t_to_s[c2] = c1
        
        return True
