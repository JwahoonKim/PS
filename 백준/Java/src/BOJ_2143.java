import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2143 {
    static long T;
    static int N, M;
    static int[] A, B;
    static long answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        B = new int[M];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        Map<Long, Long> subA = new HashMap<>();
        Map<Long, Long> subB = new HashMap<>();

        // A의 부 배열로 얻을 수 있는 합과 그 합의 개수 구하기
        for (int i = 0; i < N; i++) {
            long sum = 0;
            for (int j = i; j < N; j++) {
                sum += A[j];
                Long count = subA.getOrDefault(sum, 0L);
                subA.put(sum, count + 1);
            }
        }

        // B의 부 배열로 얻을 수 있는 합과 그 합의 개수 구하기
        for (int i = 0; i < M; i++) {
            long sum = 0;
            for (int j = i; j < M; j++) {
                sum += B[j];
                Long count = subB.getOrDefault(sum, 0L);
                subB.put(sum, count + 1);
            }
        }

        for (Map.Entry<Long, Long> entry : subA.entrySet()) {
            Long aKey = entry.getKey();
            Long aValue = entry.getValue();
            long bKey = T - aKey;
            Long bValue = subB.getOrDefault(bKey, 0L);
            answer += (aValue * bValue);
        }

        System.out.println(answer);
    }
}
