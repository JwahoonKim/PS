import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_6603 {

    public static final int LOTTO_COUNT = 6;
    static List<Integer> origin;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());

            if (N == 0)
                break;

            origin = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                origin.add(Integer.parseInt(st.nextToken()));
            }

            dfs(new ArrayList<>(), 0);
            System.out.println();
        }
    }

    private static void dfs(List<Integer> now, int cursor) {
        if (now.size() == LOTTO_COUNT) {
            print(now);
            return;
        }

        if (cursor >= origin.size())
            return;

        if (now.size() + (origin.size() - cursor) < LOTTO_COUNT)
            return;

        List<Integer> next1 = new ArrayList<>(now);
        List<Integer> next2 = new ArrayList<>(now);
        next1.add(origin.get(cursor));

        dfs(next1, cursor + 1);
        dfs(next2, cursor + 1);
    }

    private static void print(List<Integer> list) {
        for (Integer n : list) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
