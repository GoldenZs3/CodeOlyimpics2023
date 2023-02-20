using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static int mod = (int)1e9 + 7;

    static int CountDistinct(string S)
    {
        int n = S.Length;
        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int i = 1; i <= n; i++)
        {
            dp[i] = dp[i - 1];
            for (int j = i - 2; j <= i - 2 && j >= 0; j--)
            {
                if (S[j] != S[i - 1])
                {
                    dp[i] += dp[j];
                    dp[i] %= mod;
                }
            }
        }

        return dp[n];
    }

    static void Main(String[] args)
    {
        int N = int.Parse(Console.ReadLine());
        string S = Console.ReadLine().Trim();
        Console.WriteLine(CountDistinct(S));
    }
}