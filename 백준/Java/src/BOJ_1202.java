import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_1202 {
    static int N, K;
    static long answer = 0;
    static int[] bag;
    static int[][] jw;
    static PriorityQueue<int[]> jwQ = new PriorityQueue<>((j1, j2) -> j2[1] - j1[1]);

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        bag = new int[K];
        jw = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            jw[i][0] = Integer.parseInt(st.nextToken());
            jw[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < K; i++) {
            bag[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(bag);
        Arrays.sort(jw, Comparator.comparingInt(j -> j[0]));

        int jwCursor = 0;
        for (int i = 0; i < K; i++) {
            int m = bag[i];
            while (jwCursor < N) {
                if (jw[jwCursor][0] <= m) {
                    jwQ.add(jw[jwCursor++]);
                } else {
                    break;
                }
            }
            if (!jwQ.isEmpty())
                answer += jwQ.poll()[1];
        }

        System.out.println(answer);
    }
}
