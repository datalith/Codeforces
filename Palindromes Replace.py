word = list(input())
for n in range(len(word) // 2):
    r = word[n]
    l = word[-(n+1)]
    if r != '?' and l != '?' and r != l:
        word = ["-1"]
        break
    elif r == '?' and l == '?':
        word[n] = word[-(n + 1)] = 'a'
    elif r != '?':
        word[-(n+1)] = word[n]
    elif l != '?':
        word[n] = word[-(n + 1)]

if len(word)%2 != 0 and word[len(word)//2] == '?':
    word[len(word)//2] = 'a'
print("".join(word))
#https://codeforces.com/group/MWSDmqGsZm/contests
