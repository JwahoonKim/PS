class LeetCode_7 {
    public int reverse(long x) {
        String s = String.valueOf(x);
        boolean isMinus = false;

        if (isMinus(s)) {
            isMinus = true;
            s = s.substring(1);
        }

        String answer = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            answer += s.charAt(i);
        }

        int result;
        try {
            result = Integer.parseInt(answer);
        } catch (Exception e) {
            return 0;
        }

        if (isMinus) result *= -1;
        return result;
    }

    private static boolean isMinus(String s) {
        return s.startsWith("-");
    }
}