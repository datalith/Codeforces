# it's the same as usual way to identify odd/even numbers, but you have to ignore the values that under 2.
melonWeight = int(input())

if melonWeight % 2 == 0 and melonWeight > 2:
    print("YES")
else:
    print("NO")
