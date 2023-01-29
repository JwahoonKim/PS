public class LeetCode_5_Pointer {
    static String answer = "";
    public String longestPalindrome(String s) {
        answer = String.valueOf(s.charAt(0));

        for (int i = 0; i < s.length() - 1; i++) {
            check(s, i, 2);
            check(s, i, 1);
        }

        return answer;
    }

    private void check(String s, int start, int step) {
        if (start + step >= s.length())
            return;

        if (s.charAt(start) != s.charAt(start + step)) {
            return;
        }

        int left = start;
        int right = start + step;
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        String res = s.substring(left + 1, right);
        if (res.length() > answer.length())
            answer = res;
    }
}
