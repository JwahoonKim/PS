public class LeetCode_264 {
    public int nthUglyNumber(int n) {
        int[] nums = new int[n];
        nums[0] = 1;
        int ugly = 1;
        int a = 0, b = 0, c = 0;

        for (int i = 1; i < n; i++) {
             nums[i] = Math.min(Math.min(nums[a] * 2, nums[b] * 3), nums[c] * 5);
             ugly = nums[i];

            if (ugly == nums[a] * 2) a++;
            if (ugly == nums[b] * 3) b++;
            if (ugly == nums[c] * 5) c++;
        }

        return nums[n - 1];
    }

    public static void main(String[] args) {
        int answer = new LeetCode_264().nthUglyNumber(10);
        System.out.println("answer = " + answer);
    }
}
