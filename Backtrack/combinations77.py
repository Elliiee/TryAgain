def combine(self, n: int, k: int) ->List[List[int]]:
    path, result = [], []

    def backtrack(n, k, startNum):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startNum, n - (k - len(path)) + 2):
            path.append(i)
            backtrack(n, k, i+1)
            path.pop()
    backtrack(n, k, 1)
    return result 

print("test")