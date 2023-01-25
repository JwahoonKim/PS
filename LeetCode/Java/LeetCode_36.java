import java.util.HashSet;
import java.util.Set;

public class LeetCode_36 {
    public boolean isValidSudoku(char[][] board) {
        return isValidRow(board) && isValidCol(board) && isValidBox(board);
    }

    private boolean isValidBox(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int startRow = i * 3;
                int startCol = j * 3;
                Set<Character> set = new HashSet<>();
                for (int k = startRow; k < startRow + 3; k++) {
                    for (int l = startCol; l < startCol + 3; l++) {
                        if (board[k][l] != '.') {
                            if (set.contains(board[k][l])) {
                                return false;
                            }
                            set.add(board[k][l]);
                        }
                    }
                }
            }
        }
        return true;
    }

    private boolean isValidCol(char[][] board) {
        for (int i = 0; i < 9; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (set.contains(board[i][j])) {
                        return false;
                    }
                    set.add(board[i][j]);
                }
            }
        }
        return true;
    }

    private boolean isValidRow(char[][] board) {
        for (int i = 0; i < 9; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    if (set.contains(board[j][i])) {
                        return false;
                    }
                    set.add(board[j][i]);
                }
            }
        }
        return true;
    }
}
