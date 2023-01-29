import java.util.*;

public class LeetCode_49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            String sortedString = getSortedString(str);
            List<String> value = map.getOrDefault(sortedString, new ArrayList<>());
            value.add(str);
//            map.put(sortedString, value);
        }
        return new ArrayList<>(map.values());
    }

    private static String getSortedString(String str) {
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }

    public static void main(String[] args) {
        new LeetCode_49().groupAnagrams(new String[] {"eat","tea","tan","ate","nat","bat"});
    }
}
