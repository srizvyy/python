# Given two strings. The task is to check whether the given strings are anagrams of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

# Input: str1 = “listen”  str2 = “silent”
# Output: “Anagram”
# Explanation: All characters of “listen” and “silent” are the same.

# Input: str1 = “gram”  str2 = “arm”
# Output: “Not Anagram”


# listen 
# silent 
# sort both strings 
# loop over the strings to check if they are equal 
# if == then print anagram 
# if not == then print not anagram 
# comparison based sorting algo requires at least n log n time complexity
def anagram(str, str2):
    arr = sorted(str)
    arr2 = sorted(str2)
    sorted_str_one = ""
    sorted_str_two = ""
    for char in arr:
        arr.sort()
        sorted_str_one += char
    
    for char in arr2:
        arr2.sort()
        sorted_str_two += char
    
    
    if sorted_str_one == sorted_str_two:
        return "anagram"
    else:
        return "not anagram"
    
# print(anagram("listen", "silent"))
# print(anagram("like", "boy"))
# print(anagram("", ""))
# print(anagram("", "abc"))
# print(anagram("astronomer", "moon starer"))
# print(anagram("hello world", "world hello"))
# print(anagram("Debit card", "Bad credit"))


# hashmap 

# run two loops -> one for str_one and other for str_two 
# first loop will increment the value of each char by 1 
# second loop will decrement the value of each char by 1 
# in the end if all the values == to 0 then we have an anagram as both string have the same chars
def hashmap_anagram(str_one, str_two):
    anagram_map = {}

    str_one = str_one.replace(" ", "").lower()
    str_two = str_two.replace(" ", "").lower()

    if len(str_one) != len(str_two):
        return "not anagram because string length does not match"

    for char in str_one:
        if char in anagram_map:
            anagram_map[char] += 1
        else:
            anagram_map[char] = 1
    
    for char in str_two:
        if char in anagram_map:
            anagram_map[char] -= 1
        else:
            anagram_map[char] = 1

    for char in anagram_map:
        if anagram_map[char] == 0:
            return "anagram"
        else:
            return "not anagram"

print(hashmap_anagram("silent", "listen"))
print(hashmap_anagram("like", "boy"))
print(hashmap_anagram("hello world", "world hello"))

