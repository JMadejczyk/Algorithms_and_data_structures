# Find the LCS length for ”AGGTAB” and ”GXTXAYB”.

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of longest common subsequence
    lon_con_sub = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build lcs table (bottom up)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lon_con_sub[i][j] = lon_con_sub[i - 1][j - 1] + 1
            else:
                lon_con_sub[i][j] = max(lon_con_sub[i - 1][j], lon_con_sub[i][j - 1])
    
    return lon_con_sub[m][n]

result = lcs_length("AGGTAB", "GXTXAYB")
print("Length of lcs for 'AGGTAB' and 'GXTXAYB':", result)