package 프로그래머스.Java.src;

import java.util.LinkedList;
import java.util.Queue;

public class 프린터 {

    public int solution(int[] priorities, int location) {
        int answer = 0;

        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            q.add(new int[] {priorities[i], i});
        }

        while(!q.isEmpty()) {
            int[] poll = q.poll();
            int num = poll[0];
            int idx = poll[1];

            // 더 큰 수가 있다면 뒤로
            if (hasBigger(q, num))
                q.add(poll);

            // 더 큰 수가 없다면 빼기
            else {
                answer++;
                if (location == idx) {
                    break;
                }
            }
        }
        return answer;
    }

    private boolean hasBigger(Queue<int[]> q, int num) {
        return q.stream().anyMatch(ints -> num < ints[0]);
    }
}