import java.util.ArrayList;
import java.util.List;

public class LeetCode_39 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < candidates.length; i++) {
            List<Integer> path = new ArrayList<>();
            path.add(candidates[i]);
            calc(candidates, target, i, path, candidates[i], answer);
        }
        return answer;
    }

    private void calc(int[] candidates, int target, int startIndex, List<Integer> path, int sum, List<List<Integer>> answer) {
        if (sum == target) {
            answer.add(path);
            return;
        }

        if (sum > target) {
            return;
        }

        for (int i = startIndex; i < candidates.length; i++) {
            List<Integer> nextPath = new ArrayList<>(path);
            nextPath.add(candidates[i]);
            calc(candidates, target, i, nextPath, sum + candidates[i], answer);
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> answer = new LeetCode_39().combinationSum(new int[]{2, 3, 6, 7}, 7);
        System.out.println("answer = " + answer);
    }
}
