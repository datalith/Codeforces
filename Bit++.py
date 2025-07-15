'''first input is the number of operations, then you add the operations (X++ | X-- | ++X | --X) that you're going to apply to the initial Number (initialNum)'''
initialNum = 0
operations = int(input())
for _ in range(operations):
    operation = input()
    if operation == "X++" or operation == "++X":
        initialNum += 1
    elif operation == "X--" or operation == "--X":
        initialNum -= 1
print(InitialNum)

'''
input:
2
X++
X++

output:
2
'''
