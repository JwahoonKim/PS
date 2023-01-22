import java.util.Arrays;

public class LeetCode_16 {
    public int threeSumClosest(int[] nums, int target) {
        int answer = Integer.MAX_VALUE;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int first = i;
            int second = i + 1;
            int third = nums.length - 1;

            while (second < third) {
                int sum = nums[first] + nums[second] + nums[third];
                int nowDiff = Math.abs(target - sum);
                int diff = Math.abs(target - answer);
                
                if (nowDiff < diff) {
                    answer = sum;
                }

                if (sum > target) third--;
                else if (sum == target) return sum;
                else second++;
            }
        }

        return answer;
    }
}
