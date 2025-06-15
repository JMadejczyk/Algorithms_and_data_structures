# Implement Greedy III for the knapsack problem and test it on the counterexample provided. 
# Explain why it fails compared to the DP solution.

# Table 3: Greedy III Counterexample
# Item 1 2 3 4 5
# wi 2 1 4 1 3
# pi 5 4 12 2 10
# pi/wi 2.5 4 3 2 3.33
# c = 7, Greedy III selects {2, 5, 1, 4}, f = 21.
# Optimal (via DP) : {5, 3}, f ∗ = 22.

def greedy_knapsack_III(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    total_weight = 0

    for weight, value in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
        else:
            break

    return total_value

result = greedy_knapsack_III([2, 1, 4, 1, 3], [5, 4, 12, 2, 10], 7)
print("Result of Greedy III:", result)
# It fails, because it is not an optimal algorithm. It selects items based on the highest value to weight ratio without considering the overall capacity, leading to suboptimal solutions. 
# The DP solution finds the optimal combination of items that maximizes the total value without exceeding the weight limit, which is not guaranteed by the greedy approach.