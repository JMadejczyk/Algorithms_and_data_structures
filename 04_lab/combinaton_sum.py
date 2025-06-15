
def combination_sum(candidates, valid, target):
    candidates.sort()
    def combination_sum_backtrack(state: list, start: int, target: int):
        total = sum(state)
        if total == target:
            valid.append(state.copy())
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            state.append(candidates[i])
            combination_sum_backtrack(state, i, target)
            state.pop()

    combination_sum_backtrack([], 0, target)
    return valid

candidates = [2, 3, 6, 7]
valid = []
target = 7
print(combination_sum(candidates, valid, target))
