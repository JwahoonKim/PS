import java.util.ArrayList;
import java.util.List;

public class LeetCode_46 {
    public List<List<Integer>> permute(int[] nums) {
        if (nums.length == 0) {
            List<List<Integer>> res = new ArrayList<>();
            res.add(new ArrayList<>());
            return res;
        }

        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int[] subArray = getSubArray(nums, i);
            var subPermute = permute(subArray);
            for (List<Integer> p : subPermute) {
                answer.add(mergeList(nums[i], p));
            }
        }
        return answer;
    }

    private List<Integer> mergeList(int n, List<Integer> p) {
        List<Integer> res = new ArrayList<>();
        res.add(n);
        res.addAll(p);
        return res;
    }

    private int[] getSubArray(int[] nums, int i) {
        int[] subArray = new int[nums.length - 1];
        for (int j = 0; j < nums.length; j++) {
            if (j == i) continue;
            if (j > i) {
                subArray[j - 1] = nums[j];
            } else {
                subArray[j] = nums[j];
            }
        }
        return subArray;
    }

    public static void main(String[] args) {
        List<List<Integer>> answer = new LeetCode_46().permute(new int[]{1, 2, 3});
        System.out.println("answer = " + answer);
    }
}
