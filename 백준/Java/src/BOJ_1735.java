import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1735 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int A1 = Integer.parseInt(st.nextToken());
        int B1 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        int A2 = Integer.parseInt(st.nextToken());
        int B2 = Integer.parseInt(st.nextToken());

        int gcd = gcd(B1, B2);

        int b1 = B1 / gcd;
        int b2 = B2 / gcd;

        int B = b1 * b2 * gcd;
        int A = A1 * b2 + A2 * b1;

        int gcd2 = gcd(A, B);
        A = A / gcd2;
        B = B / gcd2;

        System.out.println(A + " " + B);
    }

    private static int gcd(int n1, int n2) {
        if (n2 == 0)
            return n1;
        return gcd(n2, n1 % n2);
    }
}
