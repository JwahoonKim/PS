public class LeetCode_121 {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int res = 0;
        for (int i = 0; i < prices.length; i++) {
            int price = prices[i];
            if (minPrice > price) {
                minPrice = price;
                continue;
            }

            res = Math.max(res, price - minPrice);
        }
        return res;
    }
}
