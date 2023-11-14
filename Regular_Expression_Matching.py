def backtrack(cache, s, p, i, j):
    key = (i, j)
    if key in cache:
        return cache[key]

    if i == -1 and j == -1:
        cache[key] = True
        return True

    if i != -1 and j == -1:
        cache[key] = False
        return cache[key]
    
    if i == -1 and p[j] == '*':
        k = j
        while k != -1 and p[k] == '*':
            k -= 2
        if k == -1:
            cache[key] = True
            return cache[key]
        cache[key] = False
        return cache[key]
    
    if i == -1 and p[j] != '*':
        cache[key] = False
        return cache[key]

    if p[j] == '*':
        if backtrack(cache, s, p, i, j - 2):
            cache[key] = True
            return cache[key]
        
        if p[j - 1] == s[i] or p[j - 1] == '.':
            if backtrack(cache, s, p, i - 1, j):
                cache[key] = True
                return cache[key]
    
    if p[j] == '.' or s[i] == p[j]:
        if backtrack(cache, s, p, i - 1, j - 1):
            cache[key] = True
            return cache[key]

    cache[key] = False
    return cache[key]

s = "abaaa"
p = ".*"
i = len(s) -1
j = len(p) -1
cache = {}

result = backtrack(cache, s, p, i, j)
print(result)