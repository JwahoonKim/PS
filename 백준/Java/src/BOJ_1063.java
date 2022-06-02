import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1063 {

    static List<String> MOVE = new ArrayList<>(Arrays.asList("R", "L", "B", "T", "RT", "LT", "RB", "LB"));
    static List<String> COLUMN = new ArrayList<>(Arrays.asList("X", "A", "B", "C", "D", "E", "F", "G", "H"));
    static int[] dx = {1, -1, 0, 0, 1, -1, 1, -1};
    static int[] dy = {0, 0, -1, 1, 1, 1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        int kingCol = COLUMN.indexOf(String.valueOf(s[0].charAt(0)));
        int kingRow = Integer.parseInt(String.valueOf(s[0].charAt(1)));

        int stoneCol = COLUMN.indexOf(String.valueOf(s[1].charAt(0)));
        int stoneRow = Integer.parseInt(String.valueOf(s[1].charAt(1)));
        
        int N = Integer.parseInt(s[2]);

        for (int i = 0; i < N; i++) {
            String move = br.readLine();
            int idx = MOVE.indexOf(move);
            int nextKingCol = kingCol + dx[idx];
            int nextKingRow = kingRow + dy[idx];

            if (nextKingCol > 8 || nextKingCol < 1 || nextKingRow > 8 || nextKingRow < 1) 
                continue;
            
            if (nextKingCol == stoneCol && nextKingRow == stoneRow) {
                int nextStoneCol = stoneCol + dx[idx];
                int nextStoneRow = stoneRow + dy[idx];
                
                if (nextStoneCol > 8 || nextStoneCol < 1 || nextStoneRow > 8 || nextStoneRow < 1) 
                    continue;
                
                kingCol = nextKingCol;
                kingRow = nextKingRow;
                stoneCol = nextStoneCol;
                stoneRow = nextStoneRow;
                
            } else {
                kingCol = nextKingCol;
                kingRow = nextKingRow;
            }
        }

        print(kingCol, kingRow);
        print(stoneCol, stoneRow);
    }

    static void print(int col, int row) {
        System.out.println(COLUMN.get(col) + row);
    }
}
