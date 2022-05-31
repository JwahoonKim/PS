import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2490 {

    static final char[] resultArr = {'E', 'A', 'B', 'C', 'D'};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 3; i ++) {
            String s = br.readLine();
            String[] s1 = s.split(" ");
            System.out.println(resultArr[countZero(s1)]);
        }
    }

    private static int countZero(String[] s1) {
        int count = 0;
        for (String s : s1) {
            if (s.equals("0"))
                count++;
        }
        return count;
    }
}
