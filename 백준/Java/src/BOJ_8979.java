import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_8979 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] info = new int[N][4];
        for (int i = 0; i < N; i ++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
            info[i][0] = Integer.parseInt(st1.nextToken());
            info[i][1] = Integer.parseInt(st1.nextToken());
            info[i][2] = Integer.parseInt(st1.nextToken());
            info[i][3] = Integer.parseInt(st1.nextToken());
        }

        int idx = 0;
        for (int i = 0; i < N; i ++) {
            if (info[i][0] == K) {
                idx = i;
                break;
            }
        }

        int gold = info[idx][1];
        int silver = info[idx][2];
        int bronze = info[idx][3];

        int rank = 1;
        for (int[] comp : info) {
            if (comp[1] > gold) rank++;
            if (comp[1] == gold) {
                if (comp[2] > silver) rank++;
                if (comp[2] == silver) {
                    if(comp[3] > bronze) rank++;
                }
            }
        }

        System.out.println(rank);
    }
}
