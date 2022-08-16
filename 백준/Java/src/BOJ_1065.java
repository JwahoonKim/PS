import java.io.IOException;
import java.util.Scanner;

public class BOJ_1065 {
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++)
            isHansu(i);

        System.out.println(answer);
    }

    private static void isHansu(int n) {
        String number = String.valueOf(n);
        int digit = number.length();

        if (digit == 1) {
            answer++;
            return;
        }

        int[] nums = new int[digit];

        for (int i = 0; i < digit; i++) {
            nums[i] = Integer.parseInt(String.valueOf(number.charAt(i)));
        }

        int d = nums[0] - nums[1];
        for (int i = 1; i < digit - 1; i++) {
            if (d != nums[i] - nums[i + 1])
                return;
        }

        answer++;
    }

}
