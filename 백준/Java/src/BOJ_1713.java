import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1713 {
    static int N, K;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        ArrayList<int[]> pictures = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            int student = Integer.parseInt(st.nextToken());
            addPicture(pictures, student, i);
        }

        pictures.sort(Comparator.comparingInt(p -> p[0]));
        for (int[] picture : pictures) {
            System.out.print(picture[0] + " ");
        }
    }

    private static void addPicture(ArrayList<int[]> pictures, int student, int turn) {
        int idx = findStudentIndex(pictures, student);
        if (idx == -1) {
            if (pictures.size() == N) {
                pictures.sort((p1, p2) -> {
                    if (p1[1] == p2[1])
                        return p2[2] - p1[2];
                    else
                        return p2[1] - p1[1];
                });
                pictures.remove(pictures.size() - 1);
            }
            pictures.add(new int[] {student, 1, turn});
        } else {
            pictures.get(idx)[1] ++;
        }
    }

    private static int findStudentIndex(ArrayList<int[]> pictures, int student) {
        for (int i = 0; i < pictures.size(); i++) {
            if (pictures.get(i)[0] == student) {
                return i;
            }
        }
        return -1;
    }
}
