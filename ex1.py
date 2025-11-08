def find(s, n):
    # s = array of integers
    # n = target number
    
    # solution 1: (Recommend)
    for i, num in enumerate(s):
        another_num = n - num
        if another_num in s:
            j = s.index(another_num)
            if i != j:
                return [i,j]
    return None
    
    # solution 2 : (Low Efficiency)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] + s[j] == n:
                return [i,j]
    return None

# test
print(find([2,7,11,15], 9))
print(find([3,2,4], 6)) 
print(find([3,3], 6)) 
print(find([3,3], 5)) 
