import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1062 {
    static int N, K;
    static String[] words;
    static int answer = 0;
    static Set<Character> basicAlp = new HashSet<>();
    static List<Character> candidate = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        basicAlp.add('a');
        basicAlp.add('n');
        basicAlp.add('t');
        basicAlp.add('i');
        basicAlp.add('c');

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        if (K < 5) {
            System.out.println(0);
            return;
        }

        words = new String[N];
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            words[i] = s.substring(4, s.length() - 4);
        }

        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (!basicAlp.contains(c) && !candidate.contains(c)) {
                    candidate.add(c);
                }
            }
        }

        if (K - 5 >= candidate.size()) {
            System.out.println(N);
            return;
        }

        dfs(new HashSet<>(), 0);
        System.out.println(answer);
    }

    static void dfs(Set<Character> learned, int cursor) {
        // 종료 조건
        if (learned.size() == K - 5) {
            int result = 0;
            for (String word : words) {
                if (canRead(word, learned))
                    result ++;
            }
            answer = Math.max(answer, result);
        }

        if (candidate.size() <= cursor)
            return;

        // 3. 가는 경우
        // 선택
        learned.add(candidate.get(cursor));
        dfs(learned, cursor + 1);
        learned.remove(candidate.get(cursor));
        // 안선택
        dfs(learned, cursor + 1);
    }

    private static boolean canRead(String word, Set<Character> learned) {
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!learned.contains(c) && !basicAlp.contains(c))
                return false;
        }
        return true;
    }
}
