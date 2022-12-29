import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_2503 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        Set<Integer> result = new HashSet<>();
        for (int n = 123; n < 1000; n++) {
            if (isValidNumber(n))
                result.add(n);
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String answer = st.nextToken();
            int strike = Integer.parseInt(st.nextToken());
            int ball = Integer.parseInt(st.nextToken());
            result = getNewResult(result, answer, strike, ball);
        }

        System.out.println(result.size());
    }

    private static boolean isValidNumber(int n) {
        int a = n / 100;
        int b = (n % 100) / 10;
        int c = (n % 10);
        return a != b && a != c && b != c && a != 0 && b != 0 && c != 0;
    }

    private static Set<Integer> getNewResult(Set<Integer> result, String answer, int strike, int ball) {
        Set<Integer> tmp = new HashSet<>();

        for (int i = 123; i < 1000; i++) {
            if (result.contains(i) && isValidNumber(i)) {
                String number = String.valueOf(i);
                if (isMatchNumber(number, answer, strike, ball)) {
                    tmp.add(i);
                }
            }
        }

        return tmp;
    }

    private static boolean isMatchNumber(String number, String answer, int strike, int ball) {
        int strikeCount = 0;
        int ballCount = 0;

        for (int i = 0; i < 3; i++) {
            char c = number.charAt(i);
            if (answer.indexOf(c) == i) {
                strikeCount++;
                continue;
            } else if (answer.indexOf(c) != -1) {
                ballCount++;
            }
        }

        return strikeCount == strike && ballCount == ball;
    }
}
