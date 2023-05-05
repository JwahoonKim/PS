public class LeetCode_1267 {
    public int countServers(int[][] grid) {
        int numRow = grid.length;
        int numCol = grid[0].length;

        int[] rowCount = new int[numRow];
        int[] colCount = new int[numCol];

        int answer = 0;

        for (int i = 0; i < numRow; i++) {
            for (int j = 0; j < numCol; j++) {
                if (grid[i][j] == 1) {
                    rowCount[i]++;
                    colCount[j]++;
                    answer++;
                }
            }
        }

        for (int i = 0; i < numRow; i++) {
            for (int j = 0; j < numCol; j++) {
                if (grid[i][j] == 1) {
                    if (rowCount[i] == 1 && colCount[j] == 1)
                        answer--;
                }
            }
        }

        return answer;
    }
}


