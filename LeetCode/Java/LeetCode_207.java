import java.util.*;

public class LeetCode_207 {
    static boolean answer;
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        answer = true;
        Set<Integer> learned = new HashSet<>();
        Map<Integer, List<Integer>> map = new HashMap<>();

        for (int[] pre : prerequisites) {
            List<Integer> list = map.getOrDefault(pre[0], new ArrayList<>());
            list.add(pre[1]);
            map.put(pre[0], list);
        }

        for (Integer num : map.keySet()) {
            learn(num, map, learned, new HashSet<>());
            if (!answer) return false;
        }

        return true;
    }

    private void learn(Integer num, Map<Integer, List<Integer>> map, Set<Integer> learned, Set<Integer> path) {
        if (!answer) {
            return;
        }

        if (path.contains(num)) {
            answer = false;
            return;
        }

        path.add(num);

        List<Integer> nexts = map.getOrDefault(num, new ArrayList<>());
        for (Integer next : nexts) {
            if (learned.contains(next)) continue;
            learn(next, map, learned, path);
        }

        path.remove(num);
        learned.add(num);
    }

    public static void main(String[] args) {
        boolean answer = new LeetCode_207().canFinish(2, new int[][]{{1, 0}});
        System.out.println("answer = " + answer);
    }
}
