import java.io.*;
import java.util.*;

public class BOJ_1759 {
    static int L, C;
    static char[] data;
    static List<String> result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        data = new char[C];
        result = new LinkedList<>();

        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < C; i++) {
            data[i] =  st2.nextToken().charAt(0);
        }

        Arrays.sort(data);
        dfs(0, 0, 0, -1, "");

        for (String s : result) {
            System.out.println(s);
        }
    }

    static void dfs(int length, int ja, int mo, int cursor, String pwd) {
        if (length == L) {
            if( ja >= 2 && mo >= 1) {
                result.add(pwd);
            }
        } else {
            for (int i = cursor + 1; i < C; i++) {
                if (data[i] == 'a' || data[i] == 'e' ||data[i] == 'i' ||data[i] == 'o' ||data[i] == 'u') {
                    dfs(length + 1, ja, mo + 1, i, pwd + data[i]);
                } else {
                    dfs(length + 1, ja + 1, mo, i, pwd + data[i]);
                }
            }
        }
    }
}
