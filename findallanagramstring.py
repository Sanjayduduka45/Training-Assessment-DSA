# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 
def anagrams(s,p):
    n=len(s)
    k=len(p)
    res=[]
    if n<k:
        return res
    freq={}
    for i in p:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    window_freq={}
    for i in s[:k]:
        if i in window_freq:
            window_freq[i]+=1
        else:
            window_freq[i]=1
    if window_freq==freq:
        res.append(0)
    for i in range(1,n-k+1):
        window_freq[s[i-1]]-=1
        if window_freq[s[i-1]]==0:
            window_freq.pop(s[i-1])
        if s[i+k-1] in window_freq:
            window_freq[s[i+k-1]]+=1
        else:
            window_freq[s[i+k-1]]=1
        if window_freq==freq:
            res.append(i)
    return res
# s = "cbaebabacd"
# p = "abc"
s = "abab"
p = "ab"
print(anagrams(s,p))