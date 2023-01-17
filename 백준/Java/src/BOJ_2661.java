import java.util.Scanner;

public class BOJ_2661 {

    static String answer = "";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        go(N, 0, "");
        System.out.println(answer);
    }

    private static void go(int N, int now, String path) {
        if (alreadyFindAnswer(N))
            return;

        if (path.length() == N) {
            answer = path;
            return;
        }

        checkAndGo(N, now, path + "1");
        checkAndGo(N, now, path + "2");
        checkAndGo(N, now, path + "3");
    }

    private static void checkAndGo(int N, int now, String nextPath) {
        if (isOk(nextPath))
            go(N, now + 1, nextPath);
    }

    private static boolean isOk(String path) {
        int N = path.length();
        for (int i = 1; i <= N / 2; i++) {
            if (isBadSequence(path, i)) {
                return false;
            }
        }
        return true;
    }

    private static boolean isBadSequence(String path, int i) {
        String s1 = path.substring(path.length() - i);
        String s2 = path.substring(path.length() - 2 * i, path.length() - i);
        if (s1.equals(s2))
            return true;
        return false;
    }

    private static boolean alreadyFindAnswer(int N) {
        return answer.length() == N;
    }
}
