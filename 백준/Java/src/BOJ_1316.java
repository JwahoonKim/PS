import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class BOJ_1316 {
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++)
            checker(br.readLine());

        System.out.println(answer);
    }

    private static void checker(String str) {
        Set<Character> visited = new HashSet<>();
        char prev = str.charAt(0);

        for (int i = 0; i < str.length(); i++) {
            char now = str.charAt(i);
            if (now != prev && visited.contains(now))
                return;

            prev = now;
            visited.add(now);
        }

        answer++;
    }
}
