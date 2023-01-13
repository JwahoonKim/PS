import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_5427 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    static boolean flag = false;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int C = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());
            char[][] map = new char[R][C];

            Queue<int[]> fireQ = new LinkedList<>();
            Queue<int[]> nextFireQ = new LinkedList<>();
            Queue<int[]> userQ = new LinkedList<>();
            Queue<int[]> nextUserQ = new LinkedList<>();
            boolean[][] visited = new boolean[R][C];
            mapInit(C, R, map, fireQ, userQ, visited);

            answer = Integer.MAX_VALUE;
            while (!userQ.isEmpty()) {
                bfsFire(C, R, map, fireQ, nextFireQ);
                fireQ = nextFireQ;
                nextFireQ = new LinkedList<>();

                bfsUser(C, R, map, userQ, nextUserQ, visited);
                userQ = nextUserQ;
                nextUserQ = new LinkedList<>();
            }
            printAnswer(answer);
        }

    }

    private static void bfsUser(int C, int R, char[][] map, Queue<int[]> userQ, Queue<int[]> nextUserQ, boolean[][] visited) {
        while (!userQ.isEmpty()) {
            int[] user = userQ.poll();
            int ur = user[0];
            int uc = user[1];
            int count = user[2];

            if (canEscape(R, C, ur, uc)) {
                answer = Math.min(count + 1, answer);
                return;
            }

            setNextUserQ(C, R, map, nextUserQ, visited, ur, uc, count);
        }
    }

    private static void setNextUserQ(int C, int R, char[][] map, Queue<int[]> nextUserQ, boolean[][] visited, int ur, int uc, int count) {
        for (int j = 0; j < 4; j++) {
            int unr = ur + dr[j];
            int unc = uc + dc[j];
            if (0 <= unr && unr < R && 0 <= unc && unc < C) {
                if (map[unr][unc] == '.' && !visited[unr][unc]) {
                    nextUserQ.add(new int[] {unr, unc, count + 1});
                    visited[unr][unc] = true;
                }
            }
        }
    }

    private static void bfsFire(int C, int R, char[][] map, Queue<int[]> fireQ, Queue<int[]> nextFireQ) {
        while (!fireQ.isEmpty()) {
            int[] fire = fireQ.poll();
            int fr = fire[0];
            int fc = fire[1];
            setNextFireQ(C, R, map, nextFireQ, fr, fc);
        }
    }

    private static void setNextFireQ(int C, int R, char[][] map, Queue<int[]> nextFireQ, int fr, int fc) {
        for (int j = 0; j < 4; j++) {
            int fnr = fr + dr[j];
            int fnc = fc + dc[j];
            if (0 <= fnr && fnr < R && 0 <= fnc && fnc < C) {
                if (map[fnr][fnc] == '.') {
                    map[fnr][fnc] = '*';
                    nextFireQ.add(new int[] {fnr, fnc});
                }
            }
        }
    }

    private static void printAnswer(int answer) {
        if (answer == Integer.MAX_VALUE) System.out.println("IMPOSSIBLE");
        else System.out.println(answer);
    }

    private static void mapInit(int C, int R, char[][] map, Queue<int[]> fireQ, Queue<int[]> userQ, boolean[][] visited) throws IOException {
        for (int j = 0; j < R; j++) {
            String str = br.readLine();
            for (int k = 0; k < C; k++) {
                char now = str.charAt(k);
                if (now == '@') {
                    userQ.add(new int[] {j, k, 0});
                    visited[j][k] = true;
                }
                if (now == '*')
                    fireQ.add(new int[] {j, k});
                map[j][k] = now;
            }
        }
    }

    private static boolean canEscape(int R, int C, int r, int c) {
        return r == 0 || r == R - 1 || c == 0 || c == C - 1;
    }
}
