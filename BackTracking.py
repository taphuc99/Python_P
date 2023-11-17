def backtrack(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x
            for y in backtrack(1, s)
            for x in backtrack(list - 1, s)
        ]
     
print(backtrack(1, ["A", "B", "C"]))
print(backtrack(2, ["A", "B", "C"]))
