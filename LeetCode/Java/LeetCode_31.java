public class LeetCode_31 {
    public void nextPermutation(int[] nums) {
        int left = findLeft(nums);
        int right = findRight(nums, left);

        swap(nums, left, right);

        int j = left == right ? left : left + 1;
        int k = nums.length - 1;

        while (j < k) {
            swap(nums, j++, k--);
        }
    }

    private static int findRight(int[] nums, int left) {
        for (int i = left + 1; i < nums.length; i++) {
            if (nums[left] >= nums[i]) {
                return i - 1;
            }
        }
        return nums.length - 1;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private static int findLeft(int[] nums) {
        for (int i = nums.length - 1; i >= 1; i--) {
            if (nums[i] > nums[i - 1])
                return i - 1;
        }
        return 0;
    }
}
