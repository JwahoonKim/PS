import java.util.ArrayList;
import java.util.List;

class LeetCode_155 {

    private List<Integer> elems;
    private List<Integer> minElems;

    public LeetCode_155() {
        elems = new ArrayList<>();
        minElems = new ArrayList<>();
    }

    public void push(int val) {
        elems.add(val);
        pushToMinElems(val);
    }

    private void pushToMinElems(int val) {
        if (minElems.isEmpty()) {
            minElems.add(val);
            return;
        }

        int min = minElems.get(minElems.size() - 1);
        if (val < min) {
            minElems.add(val);
        } else {
            minElems.add(min);
        }
    }

    public void pop() {
        minElems.remove(minElems.size() - 1);
        elems.remove(elems.size() - 1);
    }

    public int top() {
        return elems.get(elems.size() - 1);
    }

    public int getMin() {
        return minElems.get(minElems.size() - 1);
    }
}
