def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [[]for row in range(numRows)]
    index = 0
    step = -1

    for char in s:
        rows[index].append(char)
        if index == 0:
            index += 1
        elif index == numRows - 1:
            index -= 1
        else:
            index += step
    
    for i in range(numRows):
        rows[i]=''.join(rows[i])
    
    return ''.join(rows)
    
s = "PAYPALISHIRING"
numRows = 3
result = convert(s, numRows)
print(result)