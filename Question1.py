'''Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", 
then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.'''

# function to test if str2 is an anagram of str1
def anagram(str1, str2):
    return sorted(str1) == sorted(str2)


# function to check if any anagram of s is contained in t
def Question1(s, t):
    for i in range(len(t)-len(s)+ 1):
        if anagram(t[i: i+len(s)], s):
            return True
    return False


print Question1("ad", "udacity")
# True

print Question1("21", "8789610789712")
# True

print Question1("today", "tomorrow")
# False

