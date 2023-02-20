import java.util.ArrayList;
import java.util.List;

public class LeetCode_77 {
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> candidates = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            candidates.add(i);
        }

        return combination(candidates, k);
    }

    private List<List<Integer>> combination(List<Integer> candidates, int k) {
        List<List<Integer>> res = new ArrayList<>();

        if (k == 0) {
            res.add(new ArrayList<>());
        }

        for (int i = 0; i < candidates.size(); i++) {
            List<Integer> subList = candidates.subList(i + 1, candidates.size());
            List<List<Integer>> comb = combination(subList, k - 1);
            for (List<Integer> list : comb) {
                res.add(mergeList(candidates.get(i), list));
            }
        }
        return res;
    }

    private List<Integer> mergeList(Integer n, List<Integer> list) {
        ArrayList<Integer> res = new ArrayList<>();
        res.add(n);
        res.addAll(list);
        return res;
    }
}
