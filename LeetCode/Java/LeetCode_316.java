import java.util.*;

public class LeetCode_316 {
    public String removeDuplicateLetters(String s) {
        Stack<Character> stack = new Stack<>();
        Set<Character> set = new HashSet<>();
        Map<Character, Integer> counter = makeCounter(s);

        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            counter.put(now, counter.get(now) - 1);

            if (set.contains(now))
                continue;

            while (!stack.isEmpty() && stack.peek() > now && counter.get(stack.peek()) > 0) {
                set.remove(stack.pop());
            }

            set.add(now);
            stack.push(now);
        }

        StringBuilder res = new StringBuilder();
        for (Character c : stack) {
            res.append(c);
        }
        return res.toString();
    }

    private Map<Character, Integer> makeCounter(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            Integer value = counter.getOrDefault(c, 0);
            counter.put(c, value + 1);
        }
        return counter;
    }

    public static void main(String[] args) {
        String answer = new LeetCode_316().removeDuplicateLetters("bcabc");
        System.out.println("answer = " + answer);
    }
}
