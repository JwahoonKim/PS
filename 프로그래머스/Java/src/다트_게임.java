package 프로그래머스.Java.src;

import java.util.Map;
import java.util.Stack;

public class 다트_게임 {
    public int solution(String dartResult) {
        Map<Character, Integer> map = Map.of(
                'S', 1,
                'D', 2,
                'T', 3
        );

        Stack<Integer> stack = new Stack<>();
        StringBuilder score = new StringBuilder();

        for (int i = 0; i < dartResult.length(); i++) {
            char ch = dartResult.charAt(i);
            if (Character.isDigit(ch)) {
                score.append(ch);
            } else if (map.containsKey(ch)) {
                int value = (int) Math.pow(Integer.parseInt(score.toString()), map.get(ch));
                stack.add(value);
                score = new StringBuilder();
            } else if (ch == '*') {
                if (stack.size() == 1) {
                    stack.add(stack.pop() * 2);
                } else {
                    int pre = stack.pop();
                    int prePre = stack.pop();
                    stack.add(prePre * 2);
                    stack.add(pre * 2);
                }
            } else if (ch == '#') {
                stack.add(stack.pop() * -1);
            }
        }

        return stack.stream()
                .mapToInt(integer -> integer)
                .sum();
    }

    public static void main(String[] args) {
        int answer = new 다트_게임().solution("1S2D*3T");
        System.out.println(answer);
    }
}
