import java.util.Arrays;

public class LeetCode_6 {
    public String convert(String s, int numRows) {
        String[] arr = new String[numRows];
        Arrays.fill(arr, "");

        if (numRows == 1) {
            return s;
        }

        int cursor = 0;
        boolean isDown = true;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            arr[cursor] += c;

            if (isDown) {
                cursor++;
                if (cursor == numRows) {
                    isDown = false;
                    cursor -= 2;
                }
            } else {
                cursor--;
                if (cursor == -1) {
                    isDown = true;
                    cursor += 2;
                }
            }
        }

        return getAnswer(arr);
    }

    private static String getAnswer(String[] arr) {
        StringBuilder answer = new StringBuilder();
        for (String s1 : arr) answer.append(s1);
        return answer.toString();
    }
}
