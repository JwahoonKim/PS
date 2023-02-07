public class LeetCode_238 {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];

        int leftMul = 1;
        for (int i = 0; i < nums.length; i++) {
            leftMul *= nums[i];
            left[i] = leftMul;
        }

        int rightMul = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            rightMul *= nums[i];
            right[i] = rightMul;
        }

        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                res[i] = right[1];
            } else if (i == nums.length - 1) {
                res[i] = left[nums.length - 2];
            } else {
                res[i] = left[i - 1] * right[i + 1];
            }
        }
        return res;
    }
}
