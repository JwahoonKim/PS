class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class LeetCode_2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        ListNode cursor = result;

        int carry = 0;
        while (true) {
            if (l1 == null && l2 == null && carry == 0){
                return result;
            }

            int operand1 = l1 != null ? l1.val : 0;
            int operand2 = l2 != null ? l2.val : 0;
            int sum = (operand1 + operand2 + carry) % 10;
            carry = (operand1 + operand2 + carry) / 10;

            cursor.val = sum;
            cursor = getNextNodeIfPresent(l1, l2, cursor, carry);

            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;
        }
    }

    private static ListNode getNextNodeIfPresent(ListNode l1, ListNode l2, ListNode cursor, int carry) {
        if ((l1 != null && l1.next != null) || (l2 != null && l2.next != null) || carry != 0) {
            cursor.next = new ListNode();
            cursor = cursor.next;
        }
        return cursor;
    }
}