import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BOJ_16500 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static String answer;
    static int N;
    static String[] words;

    public static void main(String[] args) throws IOException {
        init();
        boolean[] dp = new boolean[answer.length()];

        for (int i = 0; i < N; i++) {
            String word = words[i];
            if (isWordMatching(word, answer)) {
                dp[word.length() - 1] = true;
            }
        }

        for (int i = 0; i < answer.length(); i++) {
            if (dp[i]) {
                for (int j = 0; j < N; j++) {
                    String word = words[j];
                    String target = answer.substring(i + 1);
                    if (isWordMatching(word, target)) {
                        dp[i + word.length()] = true;
                    }
                }
            }
        }

        int result = dp[answer.length() - 1] ? 1 : 0;
        System.out.println(result);
    }

    private static boolean isWordMatching(String word, String target) {
        return word.length() <= target.length() && target.startsWith(word);
    }

    private static void init() throws IOException {
        answer = br.readLine();
        N = Integer.parseInt(br.readLine());
        words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }
    }
}
