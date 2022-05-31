import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1157 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().toUpperCase();

        int[] count = new int[26];

        for (int i = 0; i <input.length(); i++) {
            int idx = input.charAt(i) - 'A';
            count[idx]++;
        }

        int max = 0;
        char answer = '?';
        for (int i = 0; i < count.length; i ++) {
            if (count[i] > max) {
                max = count[i];
                answer = (char) (i + 'A');
            } else if (count[i] == max) {
                answer = '?';
            }
        }

        System.out.println(answer);
    }
}
