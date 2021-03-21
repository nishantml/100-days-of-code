# arr = [[1, 3, 5],
#      [2, 6, 9],
#      [3, 6, 9]]

arr = [[1], [2], [3]]

new_arr = sum(arr, [])
new_arr.sort()
median_idx = len(new_arr)//2
print(new_arr[median_idx])
