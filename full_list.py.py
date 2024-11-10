https://www.geeksforgeeks.org/zip-in-python/

https://www.geeksforgeeks.org/python-map-function/

https://www.geeksforgeeks.org/python-list-slicing/

https://www.w3schools.com/python/ref_string_strip.asp

https://www.geeksforgeeks.org/difference-between-find-and-index-in-python/

intervals.sort(key = lambda x:x[1])

https://leetcode.com/problems/non-overlapping-intervals

https://leetcode.com/problem-list/oqv95d22/

"CompanyX".isalpha() # True, a-z, include A-Z

"hello world!".islower() # True, only check alphabet letters

print(~3)

"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
l = [2, 5, 7, 8 ,9]
for i in range(len(l)):
    print(l[~i]) # 9, 8, 7, 5, 2

def is_palindrome(s):
     return all([s[i] == s[~i] for i in range(len(s)//2)])


# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.

max([10,25,11,19], key= lambda x: x%10) 

count = 5
f"count: {count}"

# prev -> curr
curr = prev = None
curr.next, curr, prev = prev, curr.next, curr

# functools.reduce vs itertools.accumulate 
# https://indhumathychelliah.com/2020/08/18/reduce-vs-accumulate-in-python/