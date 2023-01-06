import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_5014 {
    static int F, S, G, U, D;
    public static void main(String[] args) throws IOException {
        init();
        boolean[] visited = new boolean[F + 1];

        int answer = -1;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {S, 0});
        while (!q.isEmpty()) {
            int[] now = q.poll();
            int floor = now[0];
            int count = now[1];

            if (visited[floor])
                continue;

            visited[floor] = true;
            if (floor == G) {
                answer = count;
                break;
            }

            if (canGoUp(visited, floor)) q.add(new int[]{floor + U, count + 1});
            if (canGoDown(visited, floor)) q.add(new int[]{floor - D, count + 1});
        }

        if (answer == -1)
            System.out.println("use the stairs");
        else
            System.out.println(answer);
    }

    private static boolean canGoDown(boolean[] visited, int floor) {
        return floor - D >= 1 && !visited[floor - D];
    }

    private static boolean canGoUp(boolean[] visited, int floor) {
        return floor + U <= F && !visited[floor + U];
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        F = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        U = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
    }
}
