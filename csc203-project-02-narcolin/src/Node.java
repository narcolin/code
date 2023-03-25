public class Node
{
    public int digit;
    public Node next;

    Node(int digit, Node next)
    {
        this.digit = digit;
        this.next = next;
    }
    public boolean equals(Node result) {
        if (result.next == null) {
            return false;
        }
        Node node1 = (Node)result;
        if (node1.next == result.next && node1.next.next == result.next.next && node1.digit == result.digit) {
            return true;
        }
        return this.equals(result);
    }
}
