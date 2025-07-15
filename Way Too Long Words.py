# it's simple, first input is the number of the words you're going to check, afte
inputsNum = int(input())
for _ in range(inputsNum):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])  #We don't include the length of the words we already used (word[1] & word[2]).
    else:
        print(word)
