import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_1991 {
    static Map<String, String[]> treeInfo = new HashMap<>();
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String s1 = st.nextToken();
            String s2 = st.nextToken();
            String s3 = st.nextToken();
            treeInfo.put(s1, new String[] {s2, s3});
        }

        System.out.println(preOrder("A"));
        System.out.println(inOrder("A"));
        System.out.println(postOrder("A"));
    }

    private static String postOrder(String now) {
        if (now.equals("."))
            return "";
        String[] nodes = treeInfo.get(now);
        String left = nodes[0];
        String right = nodes[1];
        return postOrder(left) + postOrder(right) + now;
    }

    private static String inOrder(String now) {
        if (now.equals("."))
            return "";
        String[] nodes = treeInfo.get(now);
        String left = nodes[0];
        String right = nodes[1];
        return inOrder(left) + now + inOrder(right);
    }

    private static String preOrder(String now) {
        if (now.equals("."))
            return "";
        String[] nodes = treeInfo.get(now);
        String left = nodes[0];
        String right = nodes[1];
        return now + preOrder(left) + preOrder(right);
    }
}
