import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_3055 {
    static int R, C;
    static int[] dx = new int[] {1,-1,0,0};
    static int[] dy = new int[] {0,0,1,-1};
    static char[][] map;
    static Queue<int[]> Q = new LinkedList<>();
    static int answer = -1;
    static int WATER = 0;
    static int HEDGE_HOG = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
                if (map[i][j] == 'S')
                    Q.add(new int[] {i, j, 0, HEDGE_HOG});
                if (map[i][j] == '*')
                    Q.add(new int[] {i, j, 0, WATER});
            }
        }

        // 물 먼저 움직일 수 있도록 조정
        if (Q.peek()[3] == HEDGE_HOG)
            Q.add(Q.poll());

        BFS(R, C);

        // 정답 출력
        if (answer == -1)
            System.out.println("KAKTUS");
        else
            System.out.println(answer);
    }

    private static void BFS(int R, int C) {
        // BFS 시작
        int turn = 0;
        while (!Q.isEmpty()) {
            while(!Q.isEmpty() && Q.peek()[2] == turn) {
                int[] poll = Q.poll();
                int y = poll[0];
                int x = poll[1];
                int dist = poll[2];
                int type = poll[3];

                for (int i = 0; i < 4; i++) {
                    int ny = y + dy[i];
                    int nx = x + dx[i];
                    if (0 <= nx && nx < C && 0 <= ny && ny < R) {
                        if (type == WATER) { // 물이 이동하는 경우
                            if (map[ny][nx] != 'D' && map[ny][nx] != 'X' && map[ny][nx] != '*') {
                                map[ny][nx] = '*';
                                Q.add(new int[]{ny, nx, turn + 1, WATER});
                            }
                        } else { // 고슴도치가 움직이는 경우
                            if (map[ny][nx] != '*' && map[ny][nx] != 'X' && map[ny][nx] != 'S') {
                                if (map[ny][nx] == 'D') {
                                    answer = dist + 1;
                                    return;
                                } else {
                                    map[ny][nx] = 'S';
                                    Q.add(new int[]{ny, nx, dist + 1, HEDGE_HOG});
                                }
                            }
                        }
                    }
                }
            }
            turn++;
        }
    }
}
