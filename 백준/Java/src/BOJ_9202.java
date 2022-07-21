import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class BOJ_9202 {
    static int w;
    static int score;
    static String answer;
    static int count;
    static boolean[][] visited;
    static char[][] board;
    static int[] dx = new int[] {-1,-1,-1,0,0,1,1,1};
    static int[] dy = new int[] {-1,0,1,-1,1,-1,0,1};
    static Map<Integer, Integer> scoreMap = new HashMap<>();
    static Node root = new Node();

    public static void main(String[] args) throws IOException {
        scoreMap.put(1, 0);
        scoreMap.put(2, 0);
        scoreMap.put(3, 1);
        scoreMap.put(4, 1);
        scoreMap.put(5, 2);
        scoreMap.put(6, 3);
        scoreMap.put(7, 5);
        scoreMap.put(8, 11);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        w = Integer.parseInt(br.readLine());

        for (int i = 0; i < w; i++) {
            String word = br.readLine();
            insertWord(word);
        }
        br.readLine();

        int b = Integer.parseInt(br.readLine());
        for (int i = 0; i < b; i++) {
            score = 0;
            count = 0;
            answer = "";
            board = new char[4][4];
            visited = new boolean[4][4];

            for (int j = 0; j < 4; j++) {
                String line = br.readLine();
                for (int k = 0; k < 4; k++) {
                    board[j][k] = line.charAt(k);
                }
            }
            br.readLine();

            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (root.hasChild(board[j][k]))
                        dfs(j,k,root.getChild(board[j][k]));
                }
            }
            System.out.println(score + " " + answer + " " + count);
            root.resetHit();
        }
    }

    private static void dfs(int y, int x, Node node) {
        // 체크인
        visited[y][x] = true;
        // 목적지인가?
        if (node.isWord && !node.isHit) {
            node.isHit = true;
            String content = node.content;
            int len = content.length();
            count += 1;
            score += scoreMap.get(len);
            if (len == answer.length() && content.compareTo(answer) < 0) {
                answer = content;
            } else if (len > answer.length()) {
                answer = content;
            }
        }
        // 연결된 곳 확인
        for (int k = 0; k < 8; k++) {
            int nx= x + dx[k];
            int ny = y + dy[k];
            // 갈수있는가?
            if (0 <= nx && nx < 4 && 0 <= ny && ny < 4 && !visited[ny][nx]) {
                char next = board[ny][nx];
                if (node.hasChild(next)) {
                    Node child = node.getChild(next);
                    dfs(ny, nx, child);
                }
            }
        }
        // 체크아웃
        visited[y][x] = false;
    }

    private static void insertWord(String word) {
        Node current = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (current.child[c - 'A'] == null)
                current.child[c - 'A'] = new Node();
            current = current.child[c - 'A'];
        }
        current.isWord = true;
        current.content = word;
    }

    static class Node {
        boolean isWord;
        boolean isHit;
        String content;
        Node[] child = new Node[26];

        boolean hasChild(char c) {
            return child[c - 'A'] != null;
        }

        Node getChild(char c) {
            return child[c - 'A'];
        }

        void resetHit() {
            isHit = false;
            for (int i = 0; i < 26; i++) {
                if (child[i] != null)
                    child[i].resetHit();
            }
        }
    }
}
