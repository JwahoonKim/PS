public class LeetCode_200 {
    public int numIslands(char[][] grid) {
        int answer = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    answer++;
                    dfs(i, j, grid, visited);
                }
            }
        }

        return answer;
    }

    private void dfs(int i, int j, char[][] grid, boolean[][] visited) {
        if (canNotGo(i, j, grid, visited))
            return;

        visited[i][j] = true;

        dfs(i + 1, j, grid, visited);
        dfs(i - 1, j, grid, visited);
        dfs(i, j + 1, grid, visited);
        dfs(i, j - 1, grid, visited);
    }

    private boolean canNotGo(int i, int j, char[][] grid, boolean[][] visited) {
        if (0 <= i && i < grid.length && 0 <= j && j < grid[0].length)
            return grid[i][j] != '1' || visited[i][j];
        return true;
    }

    public static void main(String[] args) {
        char[][] grid = {
                {'1','1','0','0','0'},
                {'1','1','0','0','0'},
                {'0','0','1','0','0'},
                {'0','0','0','1','1'}
        };
        new LeetCode_200().numIslands(grid);
    }
}
