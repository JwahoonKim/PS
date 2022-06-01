import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_3048 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int aCount = Integer.parseInt(st.nextToken());
        int bCount = Integer.parseInt(st.nextToken());

        List<Ant> ants = new ArrayList<>(101);
        String groupA = br.readLine();
        String groupB = br.readLine();

        for (int i = aCount - 1; i >= 0; i--) {
            ants.add(new Ant(0, groupA.charAt(i)));
        }

        for (int i = 0; i < bCount; i ++) {
            ants.add(new Ant(1, groupB.charAt(i)));
        }

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            for (int j = 0; j < ants.size() - 1; j++) {
                Ant now = ants.get(j);
                Ant next = ants.get(j + 1);
                if (now.dir + 1 == next.dir) {
                    ants.set(j, next);
                    ants.set(j + 1, now);
                    j++;
                }
            }
        }

        // 1번 출력 방식 (ants는 ArrayList<Ant>) 속도 왜이리 차이나지..?
//        ants.forEach(ant -> System.out.print(ant.name));

        // 2번 출력 방식
        for (Ant ant : ants) {
            System.out.print(ant.name);
        }

    }

    static class Ant {
        int dir;
        char name;

        public Ant(int dir, char name) {
            this.dir = dir;
            this.name = name;
        }
    }
}
