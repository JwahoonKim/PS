public class LeetCode_79 {
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};
    static boolean alreadyFindAnswer = false;

    public boolean exist(char[][] board, String word) {
        alreadyFindAnswer = false;
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (word.charAt(0) == board[i][j]) {
                    String start = String.valueOf(board[i][j]);
                    visited[i][j] = true;
                    go(board, word, i, j, visited, start);
                    visited[i][j] = false;
                }
            }
        }
        return alreadyFindAnswer;
    }

    private void go(char[][] board, String word, int r, int c, boolean[][] visited, String path) {
        if (path.equals(word)) {
            alreadyFindAnswer = true;
            return;
        }

        if (alreadyFindAnswer)
            return;

        for (int i = 0; i < 4; i++) {
            int nextR = r + dr[i];
            int nextC = c + dc[i];
            if (isInBoard(board, nextR, nextC)) {
                if (canGoNextCell(board, word, visited, path, nextR, nextC)) {
                    visited[nextR][nextC] = true;
                    go(board, word, nextR, nextC, visited, path + board[nextR][nextC]);
                    visited[nextR][nextC] = false;
                }
            }
        }

    }

    private static boolean canGoNextCell(char[][] board, String word, boolean[][] visited, String path, int nextR, int nextC) {
        return !visited[nextR][nextC] && board[nextR][nextC] == word.charAt(path.length());
    }

    private static boolean isInBoard(char[][] board, int nextR, int nextC) {
        return 0 <= nextR && nextR < board.length && 0 <= nextC && nextC < board[0].length;
    }

    public static void main(String[] args) {
        new LeetCode_79().exist(new char[][]{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}}, "SEE");
    }
}

