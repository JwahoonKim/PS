public class LeetCode_11 {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;

        while(left != right) {
            int leftH = height[left];
            int rightH = height[right];
            int h = Math.min(rightH, leftH);
            maxArea = Math.max(maxArea, h * (right - left));

            if (leftH < rightH) left++;
            else right--;
        }

        return maxArea;
    }
}
