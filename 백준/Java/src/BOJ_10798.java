import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class BOJ_10798 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] stringArr = new String[5];

        final int NUM_WORDS = 5;
        int maxLength = 0;

        for (int i = 0; i < NUM_WORDS; i++) {
            String s = br.readLine();
            if (s.length() > maxLength) maxLength = s.length();
            stringArr[i] = s;
        }

        for (int i = 0; i < maxLength; i ++) {
            for (int j = 0; j < NUM_WORDS; j ++) {
                String now = stringArr[j];
                if (now.length() <= i) continue;
                sb.append(now.charAt(i));
            }
        }

        System.out.println(sb);
    }
}
