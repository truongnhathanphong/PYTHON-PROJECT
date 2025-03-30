with open("474.INP") as filein:
    m, n = map(int, filein.readline().strip().split(" "))
    a = list(map(str, filein.readline().strip().split(" ")))

dp = [[0] * (n + 1) for i in range(m + 1)]

for s in a:
    ones = s.count("1")
    zeroes = s.count("0")
    for i in range(m, zeroes - 1, -1):
        for j in range(n, ones - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)

print(dp)