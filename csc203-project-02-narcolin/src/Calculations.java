public class Calculations {
    public static Node Addition(Node list1, Node list2) {
        int carry = 0;
        Node result = null;
        Node iter = null;
        int sum = 0;
        while (list1 != null || list2 != null) {
            sum = carry;
            if (list1 != null) {
                sum = sum + list1.digit;
                list1 = list1.next;
            }

            if (list2 != null) {
                sum = sum + list2.digit;
                list2 = list2.next;
            }
            carry = sum / 10;
            sum = sum % 10;
            if(result == null)
            {
                iter = new Node(sum, null);
                result = iter;
            }
            else
            {
                iter.next = new Node(sum, null);
                iter = iter.next;
            }
        }
        if (carry != 0) {
            iter.next = new Node(carry, null);
        }
        return result;
    }
    public static Node Multiplication(Node l1, Node l2) {
        int rows = 0; // determines how many 0s we add at the end
        int product = 0;
        int carry = 0;
        Node answer = new Node(0, null);
        while (l2 != null) {
            Node copy = l1;
            Node result = null;
            Node iter = null;
            for (int i = 0; i < rows; i++) {
                if (iter == null) {
                    iter = new Node(0, null);
                    result = iter;
                } else {
                    iter.next = new Node(0, null);
                    iter = iter.next;
                }
            }
            while (copy != null) {
                product = copy.digit * l2.digit + carry;
                carry = product / 10;
                product = product % 10;
                if (result == null) {
                    iter = new Node(product, null);
                    result = iter;
                } else {
                    iter.next = new Node(product, null);
                    iter = iter.next;
                }
                copy = copy.next;
            }
            if (carry != 0) {
                iter.next = new Node(carry, null);
                iter = iter.next;
            }
            rows++;
            answer = Addition(answer, result);
            l2 = l2.next;
        }
        return answer;
    }
    public static Node Exponentiation(Node l1, int n) {
        Node squared = Multiplication(l1, l1);
        Node answer = squared;
        if (n % 2 == 0) {
            int power = n / 2;
            while (power > 1) {
                answer = Multiplication(answer, squared);
                power--;
            }
        } else {
            int power = (n - 1) / 2;
            while (power > 1) {
                answer = Multiplication(answer, squared);
                power--;
            }
            answer = Multiplication(answer, l1);
        }
        return answer;
    }
}