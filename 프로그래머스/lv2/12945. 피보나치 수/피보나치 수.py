def solution(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append((dp[i-1]%1234567) + (dp[i-2] % 1234567))
    answer = dp[n] % 1234567
    return answer