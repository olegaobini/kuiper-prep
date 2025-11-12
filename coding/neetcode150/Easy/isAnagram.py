from collections import defaultdict
def isAnagram( s: str, t: str):
        '''
        initial validation, if different lengths -> not anagram ?

        go through chars in s, append to dictionary, 
        '''

        s_chars = {}
        t_chars = {}


        if len(s) != len(t):
             return False

        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1

        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        return s_chars == t_chars

print(isAnagram("hello", "olleh"))

