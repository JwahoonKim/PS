import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7562 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[][] move = {
            {1, 2}, {1, -2}, {-1, 2}, {-1, -2},
            {2, 1}, {2, -1}, {-2, 1}, {-2, -1}
    };

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            System.out.println(calc());
        }
    }

    private static int calc() throws IOException {
        int I = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int startR = Integer.parseInt(st.nextToken());
        int startC = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int endR = Integer.parseInt(st.nextToken());
        int endC = Integer.parseInt(st.nextToken());

        int answer = 0;
        boolean visited[][] = new boolean[I][I];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] { startR, startC, 0 });
        visited[startR][startC] = true;

        while(!q.isEmpty()) {
            int[] now = q.poll();
            int r = now[0];
            int c = now[1];
            int count = now[2];

            if (r == endR && c == endC) {
                answer = count;
                break;
            }

            for (int i = 0; i < move.length; i++) {
                int dr = r + move[i][0];
                int dc = c + move[i][1];

                if (0 <= dr && dr < I && 0 <= dc && dc < I && !visited[dr][dc]) {
                    q.add(new int[] { dr, dc, count + 1});
                    visited[dr][dc] = true;
                }
            }
        }
        return answer;
    }
}
