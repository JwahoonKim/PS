public class LeetCode_42 {
    public int trap(int[] height) {
        int[] maxHeightAndIndex = find(height);
        int maxHeight = maxHeightAndIndex[0];
        int maxIndex = maxHeightAndIndex[1];
        int sum = 0;
        int leftMax = 0;
        int rightMax = 0;

        for (int i = 0; i < maxIndex; i++) {
            if (leftMax <= height[i]) {
                leftMax = height[i];
                continue;
            }
            sum += (leftMax - height[i]);
        }

        for (int i = height.length - 1; i > maxIndex; i--) {
            if (rightMax <= height[i]) {
                rightMax = height[i];
                continue;
            }
            sum += (rightMax - height[i]);
        }

        return sum;
    }

    private int[] find(int[] height) {
        int max = 0;
        int index = 0;
        for (int i = 0; i < height.length; i++) {
            if (height[i] > max) {
                max = height[i];
                index = i;
            }
        }
        return new int[] {max, index};
    }
}
