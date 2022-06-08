package 프로그래머스.Java.src;

import java.util.*;

public class Solution {
    static int answer = 0;
    static Set<Integer> result = new HashSet<>();

    public int solution(String numbers) {
        int size = numbers.length();
        List<String> nums = Arrays.asList(numbers.split(""));

        for (int i = 1; i <= size; i++) {
            permutation("", nums, i);
        }

        for (int num : result) {
            if (isPrime(num))
                answer++;
        }

        return answer;
    }

    private void permutation(String path, List<String> nums, int count) {
        if (count == 0) {
            if (path.charAt(0) != '0') {
                result.add(Integer.valueOf(path));
            }
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            List<String> next = new ArrayList<>();
            next.addAll(nums.subList(0, i));
            next.addAll(nums.subList(i + 1, nums.size()));
            permutation(path + nums.get(i), next, count - 1);
        }
    }

    public boolean isPrime(int num) {
        if (num == 1)
            return false;
        for (int i = 2; i <= (int)Math.sqrt(num); i ++) {
            if (num % i == 0)
                return false;
        }
        return true;
    }
}
