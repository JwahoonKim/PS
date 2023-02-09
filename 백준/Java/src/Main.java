import java.util.Scanner;

class Main {

    public static final int MAX_NUMBER = 1000001;
    static long[] nums = new long[MAX_NUMBER + 1];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long k = sc.nextInt();
        nums[1] = 1;
        for (int i = 1; i < MAX_NUMBER; i++) {
            for (int j = 2 * i; j < MAX_NUMBER; j += i)
                nums[j] -= nums[i];
        }

        long left = 0;
        long right = Integer.MAX_VALUE;
        while (left < right - 1) {
            long mid = (left + right) / 2;
            if (check(mid) < k)
                left = mid;
            else
                right = mid;
        }
        System.out.println(right);
    }

    private static long check(long k) {
        long cnt = 0;
        for (long i = 1; i * i <= k; i++) {
            cnt += nums[(int) i] * k / (i * i);
        }
        return cnt;
    }


}