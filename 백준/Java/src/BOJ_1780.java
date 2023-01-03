import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1780 {
    static int minusOneCount = 0;
    static int zeroCount = 0;
    static int oneCount = 0;
    static int[][] paper;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        paper = new int[N][N];
        initPaper(br, N);
        countPaper(paper, N, 0, 0);
        printResult();
    }

    private static void printResult() {
        System.out.println(minusOneCount);
        System.out.println(zeroCount);
        System.out.println(oneCount);
    }

    private static void countPaper(int[][] paper, int n, int r, int c) {
        if (isSamePaper(paper, n, r, c)) {
            int base = paper[r][c];
            if (base == -1) {
                minusOneCount++;
            } else if (base == 0) {
                zeroCount++;
            } else if (base == 1) {
                oneCount++;
            }
        } else {
            for (int i = 0; i < 3; i++) {
                int nextN = n / 3;
                countPaper(paper, nextN, r + i * nextN, c);
                countPaper(paper, nextN, r + i * nextN, c + nextN);
                countPaper(paper, nextN, r + i * nextN, c + 2 * nextN);
            }
        }
    }

    private static boolean isSamePaper(int[][] paper, int n, int r, int c) {
        int base = paper[r][c];
        for (int i = r; i < r + n; i++)
            for (int j = 0; j < n; j++)
                if (base != paper[i][c + j])
                    return false;
        return true;
    }

    private static void initPaper(BufferedReader br, int N) throws IOException {
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}
