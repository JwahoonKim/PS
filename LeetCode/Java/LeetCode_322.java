import java.util.Arrays;

public class LeetCode_322 {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (canChooseCoin(i, coin, dp)) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }

    private static boolean canChooseCoin(int i, int coin, int[] dp) {
        return coin <= i && dp[i - coin] != Integer.MAX_VALUE;
    }
}
