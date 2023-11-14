# def longest_common_prefix(strs: list[str]) -> str:

strs = ["flower", "flow", "flight"]
ans = ""
strs = sorted(strs)
print(strs)
first = strs[0]
print(first)
last = strs[-1]
print(last)
print(min(len(first),len(last)))
for i in range(min(len(first),len(last))):
    if(first[i]==last[i]):
        ans+=first[i]
    else:
        break
print(ans)