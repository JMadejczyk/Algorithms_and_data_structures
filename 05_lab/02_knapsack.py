# Solve the 0/1 knapsack problem for the following input:
# Item 1 2 3 4 5
# wi 1 1 2 3 3
# pi 2 1 3 7 6
# c = 7
# Verify the solution x
# ∗ = {x1, x4, x5}, f ∗ = 15.

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

knapsack_weights = [1, 1, 2, 3, 3]
knapsack_values = [2, 1, 3, 7, 6]
knapsack_capacity = 7
result = knapsack(knapsack_weights, knapsack_values, knapsack_capacity)
print(f"Maximum value in knapsack: {result}")