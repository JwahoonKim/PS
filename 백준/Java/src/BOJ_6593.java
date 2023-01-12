import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_6593 {
    static int[] dx = {1, -1, 0, 0, 0, 0};
    static int[] dy = {0, 0, 1, -1, 0, 0};
    static int[] dz = {0, 0, 0, 0, 1, -1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        while(true) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());

            if (L == 0 && R == 0 && C == 0)
                break;

            char[][][] building = new char[L][R][C];
            boolean[][][] visited = new boolean[L][R][C];
            int[][][] dist = new int[L][R][C];
            int[] start = null;
            int[] end = null;

            for (int i = 0; i < L; i++) {
                for (int j = 0; j < R; j++) {
                    String s = br.readLine();
                    for (int k = 0; k < C; k++) {
                        char now = s.charAt(k);
                        if (now == 'S') start = new int[]{i, j, k, 0};
                        if (now == 'E') end = new int[]{i, j, k, 0};
                        building[i][j][k] = now;
                    }
                }
                br.readLine();
            }

            Queue<int[]> q = new LinkedList<>();
            q.add(start);
            visited[start[0]][start[1]][start[2]] = true;
            int answer = -1;
            while (!q.isEmpty()) {
                int[] now = q.poll();
                int z = now[0];
                int y = now[1];
                int x = now[2];
                int count = now[3];

                if (x == end[2] && y == end[1] && z == end[0]) {
                    answer = count;
                    break;
                }

                dist[z][y][x] = count;

                for (int i = 0; i < 6; i++) {
                    int nz = z + dz[i];
                    int ny = y + dy[i];
                    int nx = x + dx[i];

                    if (0 <= nz && nz < L && 0 <= ny && ny < R && 0 <= nx && nx < C) {
                        if (!visited[nz][ny][nx] && building[nz][ny][nx] != '#') {
                            visited[nz][ny][nx] = true;
                            q.add(new int[]{nz, ny, nx, count + 1});
                        }
                    }
                }
            }

            System.out.println(answer == -1 ? "Trapped!" : "Escaped in " + answer + " minute(s).");
        }
    }
}
