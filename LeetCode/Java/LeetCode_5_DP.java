public class LeetCode_5_DP {
    public String longestPalindrome(String s) {
        String answer = String.valueOf(s.charAt(0));

        boolean[][] dp = new boolean[s.length()][s.length()];
        initDP(s, dp);

        for (int c = 1; c < s.length(); c++) {
            for (int r = 0; r < c; r++) {
                if (isPalindrome(s, dp, c, r)){
                    dp[r][c] = true;
                    if (canUpdateAnswer(answer, c, r)) {
                        answer = s.substring(r, c + 1);
                    }
                }
            }
        }

        return answer;
    }

    private static boolean canUpdateAnswer(String answer, int c, int r) {
        return c - r + 1 > answer.length();
    }

    private static boolean isPalindrome(String s, boolean[][] dp, int c, int r) {
        return dp[r + 1][c - 1] && s.charAt(r) == s.charAt(c);
    }

    private static void initDP(String s, boolean[][] dp) {
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < s.length(); j++) {
                if (j == 0 || i >= j)
                    dp[i][j] = true;
            }
        }
    }

    public static void main(String[] args) {
        new LeetCode_5_DP().longestPalindrome("cbbd");
    }
}
