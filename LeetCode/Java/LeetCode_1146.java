import java.util.TreeMap;

public class LeetCode_1146 {
    TreeMap<Integer, Integer>[] array;
    int snapID = 0;

    public LeetCode_1146(int length) {
        array = new TreeMap[length];
        initArray(array);
    }

    private void initArray(TreeMap<Integer, Integer>[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] = new TreeMap<>();
            array[i].put(0, 0);
        }
    }

    public void set(int index, int val) {
        array[index].put(snapID, val);
    }

    public int snap() {
        return snapID++;
    }

    public int get(int index, int snapID) {
        return array[index].floorEntry(snapID).getValue();
    }

}
