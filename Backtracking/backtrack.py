def subset_sum(arr, target):
    result = []
    def backtrack(start, path, total):
        if total == target:
            result.append(path)
            return
        if total > target:
            return
        for i in range(start, len(arr)):
            backtrack(i, path + [arr[i]], total + arr[i])
    backtrack(0, [], 0)
    return result

arr = [2, 4, 6, 8]
target = 14
print(subset_sum(arr, target))