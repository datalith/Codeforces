#Simply if two members of team agreed about the solution, They approve it, else they aren't going to approve it.
num = int(input()) #The number of contests that the team is going to vote to agree in.
approvals = 0
for i in range(num):
    votes = input()
    ones = 0
    for e in votes:
        if e == '1':
            ones += 1
    if ones >= 2:
        approvals += 1
print(approvals)


"""
example:

input:
4
1 0 0 0          <- one   agreed,  disapproved
0 1 0 1          <- two   agreed,  approved
1 1 1 1          <- all   agreed,  approved
1 1 0 1          <- three agreed,  approved

output:
3
"""
