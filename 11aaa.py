# R-4.1 Describe a recursive algorithm for finding the maximum element in a sequence, S, 
# of n elements. What is your running time and space usage? 

#answer:Using indexes, recursively call functions,++n each time, to achieve search.
# Time complexity O (n), space complexity O (n)
def find_max_index(S, n = 0):
    if n == len(S) - 1:
        return S[n]
    else:
        max = find_max_index(S, n + 1)
        return S[n] if S[n] > max else max
    
S = [3, 5, 2, 8, 1]
print(find_max_index(S, 0))

# R-4.7 Describe a recursive function for converting a string of digits into the integer it 
# represents. For example, 13531 represents the integer 13,531.

# answer:Using indexes, recursively call functions, each time++n, gradually converting them to integers by quantile.
# The time complexity is O (n), and the space complexity is 0 (n)
def string_to_int(s, n=0):
    if n == len(s):
        return 0
    c = int(s[n])
    r = string_to_int(s, n + 1)
    p = len(s) - n - 1
    return c * (10 ** p) + r
S_1 = "123"
print(string_to_int(S_1))