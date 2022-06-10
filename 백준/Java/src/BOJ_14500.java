import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14500 {

    static int[][] nemo = {{0, 0}, {1, 0}, {0, 1}, {1, 1}};
    static int[][] straight = {{0, 0}, {0, 1}, {0, 2}, {0, 3}};
    static int[][] nieun = {{0, 0}, {1, 0}, {2, 0}, {2, 1}};
    static int[][] nieun2 = {{0, 1}, {1, 1}, {2, 1}, {2, 0}};
    static int[][] riyl = {{0, 0}, {1, 0}, {1, 1}, {2, 1}};
    static int[][] riyl2 = {{0, 1}, {1, 1}, {1, 0}, {2, 0}};
    static int[][] tshape = {{0, 0}, {0, 1}, {0, 2}, {1, 1}};
    static int[][][] shapes = {nemo, straight, nieun, nieun2, riyl, riyl2, tshape};

    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] nums = new int[N][M];
        for (int i = 0; i < N; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st1.nextToken());
                nums[i][j] = num;
            }
        }

        int[][] rotateNums1 = rotate(nums);
        int[][] rotateNums2 = rotate(rotateNums1);
        int[][] rotateNums3 = rotate(rotateNums2);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                check(nums, i, j);
                check(rotateNums1, j, i);
                check(rotateNums2, i, j);
                check(rotateNums3, j, i);
            }
        }
        // 정답 출력
        System.out.println(answer);
    }

    // 맵 회전
    private static int[][] rotate(int[][] nums) {
        int x = nums[0].length;
        int y = nums.length;
        int[][] result = new int[x][y];

        for (int i = 0; i < x; i++)
            for (int j = 0; j < y; j++) {
                result[i][j] = nums[y - (j + 1)][i];
            }

        return result;
    }

    private static void check(int[][] arr, int yStart, int xStart) {
        int[] nx = new int[4];
        int[] ny = new int[4];
        int score;

        for (int[][] shape : shapes) {
            for (int j = 0; j < 4; j++) {
                nx[j] = shape[j][1] + xStart;
                ny[j] = shape[j][0] + yStart;
            }

            if (validCoordinate(nx, ny, arr)) {
                score = 0;
                for (int k = 0; k < 4; k++) {
                    score += arr[ny[k]][nx[k]];
                }
                answer = Math.max(score, answer);
            }
        }
    }

    // 맵을 벗어난 인덱스인지 체크
    private static boolean validCoordinate(int[] nx, int[] ny, int[][] arr) {
        for (int i = 0; i < 4; i++) {
            if (nx[i] < 0 || nx[i] >= arr[0].length || ny[i] < 0 || ny[i] >= arr.length)
                return false;
        }
        return true;
    }
}
