'''Question 2
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.'''


# check if string s is palindrome
def Palindrome(s):
    return s == s[::-1]

def question2(s):
    if s:
        x, m, n = 0, 0, 0
        for i in xrange(0, len(s)):
            for j in xrange(i + 1, len(s) + 1):
                pattern = s[i:j]
                if Palindrome(pattern) and len(pattern) > x:
                    x = len(pattern)
                    m, n = i, j
        result = s[m:n]
        return result

print question2("racecar")
 # racecar
print question2("apple")
 # pp
print question2("udacity")
# u
