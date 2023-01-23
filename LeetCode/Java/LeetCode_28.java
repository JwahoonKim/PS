public class LeetCode_28 {
    public int strStr(String haystack, String needle) {
        if (!haystack.contains(needle)) {
            return -1;
        }

        for (int i = 0; i < haystack.length(); i++) {
            if (haystack.substring(i).startsWith(needle)) {
                return i;
            }
        }
        return -1;
    }
}
