arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))
arr2_sum = sum(arr2)
arr3_sum = sum(arr3)

if arr2_sum == arr3_sum:
    print("Yes")
else:
    print("No")
