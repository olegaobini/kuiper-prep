'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

from types import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    '''
    1st: check for anagram in the list
     - iterate through strs and turn each element into hashmap
     - 
    2nd: Check for matching anagrams using hashmap
     - brute force
     - hashmap of hashmaps

     hashmap:
     {"char bucket":""}
    ''' 

    res = {}
    for str in strs:
        count = [0] * 26

        for char in str:
            count[ord(char) - ord(str)] += 1

        res[tuple(count)].append(str)

    return list(res.values())  #
