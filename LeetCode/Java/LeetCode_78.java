import java.util.ArrayList;
import java.util.List;

public class LeetCode_78 {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(new ArrayList<>());
        for (int i = 0; i < nums.length; i++) {
            List<Integer> path = new ArrayList<>();
            path.add(nums[i]);
            go(nums, path, i, answer);
        }
        return answer;
    }

    private void go(int[] nums, List<Integer> path, int idx, List<List<Integer>> answer) {
        answer.add(path);
        for (int i = idx + 1; i < nums.length; i++) {
            List<Integer> nextPath = new ArrayList<>(path);
            nextPath.add(nums[i]);
            go(nums, nextPath, i, answer);
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> answer = new LeetCode_78().subsets(new int[]{1, 2, 3});
        System.out.println("answer = " + answer);
    }
}
