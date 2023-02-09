import java.util.Arrays;
import java.util.Stack;

public class LeetCode_739 {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<>();
        int[] answer = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            int[] tempAndIndex = {temp, i};

            while (!stack.isEmpty() && stack.peek()[0] < temp) {
                int[] pop = stack.pop();
                answer[pop[1]] = i - pop[1];
            }
            stack.add(tempAndIndex);
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] answer = new LeetCode_739().dailyTemperatures(new int[]{73,74,75,71,69,72,76,73});
        System.out.println("answer = " + Arrays.toString(answer));
    }
}
