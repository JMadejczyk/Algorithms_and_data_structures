# Compute the edit distance between ”sunday” and ”saturday”.

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # If s1 is empty, we need j insertions
            elif j == 0:
                dp[i][j] = i  # If s2 is empty, we need i deletions
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1) # Substitution

    return dp[m][n]

result = edit_distance("sunday", "saturday")
print("Edit distance between 'sunday' and 'saturday':", result)