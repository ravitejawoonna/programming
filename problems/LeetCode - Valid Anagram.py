#https://leetcode.com/problems/valid-anagram/

def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    
    t_set = {}
    s_set = {}
    
    for l in s:
        if l in s_set:
            s_set[l] = s_set[l] + 1
        else:
            s_set[l] = 1
            
    for l in t:
        if l in t_set:
            t_set[l] = t_set[l] + 1
        else:
            t_set[l] = 1
            
    
    for key in s_set:
        if key in t_set and t_set[key] == s_set[key]:
            continue
        else:
            return False
    return True