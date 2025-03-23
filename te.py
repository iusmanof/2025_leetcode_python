strs = ["flower","flow","flight"]


result = ""
for i in range(len(min(strs, key=len))): 
    if all(s[:i+1] == strs[0][:i+1] for s in strs):
        result += strs[0][i]
    else:
        break
    
print(result)