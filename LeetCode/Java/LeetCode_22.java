import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import static java.util.stream.Collectors.toList;

public class LeetCode_22 {
    public List<String> generateParenthesis(int n) {
        List<String> allCase = new ArrayList<>();
        makeAllCase(0, n, allCase, "");
        return allCase.stream()
                .filter(this::isValid)
                .collect(toList());
    }

    private boolean isValid(String parenthesis) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < parenthesis.length(); i++) {
            char c = parenthesis.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.peek() == ')')
                    return false;
                stack.pop();
            }
        }

        return stack.isEmpty();
    }

    private void makeAllCase(int count, int n, List<String> allCase, String path) {
        if (count == n) {
            allCase.add(path);
            return;
        }
        makeAllCase(count + 1, n, allCase, path + "((");
        makeAllCase(count + 1, n, allCase, path + "()");
        makeAllCase(count + 1, n, allCase, path + ")(");
        makeAllCase(count + 1, n, allCase, path + "))");
    }

    public static void main(String[] args) {
        new LeetCode_22().generateParenthesis(8);
    }
}
