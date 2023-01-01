import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ_11000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Lecture[] lectures = new Lecture[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lectures[i] = new Lecture(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(lectures, Comparator.comparingInt(c -> c.start));
        PriorityQueue<Lecture> q = new PriorityQueue<>(Comparator.comparingInt(c -> c.end));

        int answer = 1;
        q.add(lectures[0]);
        for (int i = 1; i < N; i++) {
            Lecture curLecture = lectures[i];
            Lecture fastestEndLecture = q.poll();

            if (fastestEndLecture.end > curLecture.start) {
                q.add(fastestEndLecture);
                answer++;
            }
            q.add(curLecture);
        }

        System.out.println(answer);
    }

    static class Lecture {
        int start;
        int end;

        public Lecture(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}
