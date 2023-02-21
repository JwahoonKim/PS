import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class LeetCode_332 {
    static List<String> answer;
    public List<String> findItinerary(List<List<String>> tickets) {
        answer = new ArrayList<>();
        
        List<String> path = new ArrayList<>();
        path.add("JFK");
        int targetSize = tickets.size() + 1;
        go("JFK", tickets, path, targetSize);
        return answer;
    }

    private void go(String from, List<List<String>> tickets, List<String> path, int targetSize) {
        if (answer.size() != 0) {
            return;
        }

        if (path.size() == targetSize) {
            answer = new ArrayList<>(path);
            return;
        }
        
        List<List<String>> nextCandidates = findNextCandidates(from, tickets);
        for (List<String> next : nextCandidates) {
            tickets.remove(next);
            path.add(next.get(1));
            go(next.get(1), tickets, path, targetSize);
            path.remove(path.size() - 1);
            tickets.add(next);
        }
    }

    private List<List<String>> findNextCandidates(String from, List<List<String>> tickets) {
        List<List<String>> candidates = new ArrayList<>();
        for (List<String> ticket : tickets) {
            if (ticket.get(0).equals(from)) {
                candidates.add(ticket);
            }
        }
        candidates.sort(Comparator.comparing(c -> c.get(1)));
        return candidates;
    }
}
