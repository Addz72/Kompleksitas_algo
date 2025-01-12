def permute(array):
    result = []

    def backtrack(path, used):
        if len(path) == len(array):
            result.append(list(path))
            return

        for i in range(len(array)):
            if used[i]:
                continue
            used[i] = True
            path.append(array[i])

            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False] * len(array))
    return result

array = [3, 7, 12, 15]
result = permute(array)
print("Semua permutasi dari", array, ":", result)