import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LeetCode_17 {
    static Map<Character, char[]> map = Map.of(
            '2', new char[] {'a', 'b', 'c'},
            '3', new char[] {'d', 'e', 'f'},
            '4', new char[] {'g', 'h', 'i'},
            '5', new char[] {'j', 'k', 'l'},
            '6', new char[] {'m', 'n', 'o'},
            '7', new char[] {'p', 'q', 'r', 's'},
            '8', new char[] {'t', 'u', 'v'},
            '9', new char[] {'w', 'x', 'y', 'z'}
    );
    public List<String> letterCombinations(String digits) {
        List<String> answer = new ArrayList<>();
        List<char[]> candidates = new ArrayList<>();

        if (digits.equals(""))
            return answer;

        for (int i = 0; i < digits.length(); i++) {
            char c = digits.charAt(i);
            candidates.add(map.get(c));
        }
        dfs(0, 0, digits.length(),"", candidates, answer);
        return answer;
    }

    private void dfs(int i, int j, int targetLength, String path, List<char[]> candidates, List<String> answer) {
        if (i == targetLength) {
            answer.add(path);
            return;
        }

        char[] candidate = candidates.get(i);
        for (int k = 0; k < candidate.length; k++) {
            char now = candidate[k];
            String nextPath = path + now;
            dfs(i + 1, j, targetLength, nextPath, candidates, answer);
        }
    }

    public static void main(String[] args) {
        List<String> answer = new LeetCode_17().letterCombinations("23");
        System.out.println("answer = " + answer);
    }

}
