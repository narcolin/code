import org.junit.Test;
import static java.lang.System.lineSeparator;
import static org.junit.Assert.assertTrue;

public class CalcTest {
    @Test
    public void Test_Add () {
        Node list1 = new Node(3, null);
        list1.next = new Node(6, null);
        list1.next.next = new Node(4, null);
        System.out.print("First List: ");
        FileProcessor.printList(list1);
        System.out.println(lineSeparator());

        Node list2 = new Node(1, null);
        list2.next = new Node(8, null);
        System.out.print("Second List: ");
        FileProcessor.printList(list2);
        System.out.println(lineSeparator());

        System.out.print("Sum: ");
        Node result = Calculations.Addition(list1, list2);
        FileProcessor.printList(result);
    }
    @Test
    public void Test_Add1 () {
        Node list1 = new Node(3, null);
        list1.next = new Node(6, null);
        list1.next.next = new Node(4, null);

        Node list2 = new Node(1, null);
        list2.next = new Node(8, null);

        Node result = new Node(4, null);
        result.next = new Node(4, null);
        result.next.next = new Node(5, null);

        assertTrue(result.equals(Calculations.Addition(list1, list2)));
    }
    @Test
    public void Test_Add2 () {
        Node list1 = new Node(2, null);
        list1.next = new Node(2, null);
        list1.next.next = new Node(2, null);

        Node list2 = new Node(8, null);
        list2.next = new Node(8, null);
        list2.next.next = new Node(8, null);

        Node result = new Node(0, null);
        result.next = new Node(1, null);
        result.next.next = new Node(1, null);
        result.next.next.next = new Node(1, null);

        assertTrue(result.equals(Calculations.Addition(list1, list2)));
    }
    @Test
    public void Test_Multi() {
        Node list1 = new Node(2, null);
        list1.next = new Node(1, null);
        System.out.print("First List: ");
        FileProcessor.printList(list1);
        System.out.println(lineSeparator());

        Node list2 = new Node(2, null);
        list2.next = new Node(1, null);
        System.out.print("Second List: ");
        FileProcessor.printList(list2);
        System.out.println(lineSeparator());

        System.out.print("Product: ");
        Node result = Calculations.Multiplication(list1, list2);
        FileProcessor.printList(result);
    }
    @Test
    public void Test_Multi1() {
        Node list1 = new Node(2, null);
        list1.next = new Node(1, null);

        Node list2 = new Node(2, null);
        list2.next = new Node(1, null);

        Node list3 = new Node(0, null);
        list3.next = new Node(1, null);

        Node result1 = new Node(4, null);
        result1.next = new Node(4, null);
        result1.next.next = new Node(4, null);

        Node result2 = new Node(0, null);
        result2.next = new Node(2, null);
        result2.next.next = new Node(1, null);

        assertTrue(result1.equals(Calculations.Addition(list1, list2)));
        assertTrue(result2.equals(Calculations.Addition(list2, list3)));
    }
    @Test
    public void Test_Multi2 () {
        Node list1 = new Node(0, null);
        list1.next = new Node(0, null);
        list1.next.next = new Node(1, null);

        Node list2 = new Node(0, null);
        list2.next = new Node(8, null);

        Node result = new Node(0, null);
        result.next = new Node(0, null);
        result.next.next = new Node(0, null);
        result.next.next.next = new Node(8, null);

        assertTrue(result.equals(Calculations.Addition(list1, list2)));
    }
    @Test
    public void Test_Expo() {
        Node list1 = new Node(2, null);
        list1.next = new Node(1, null);
        System.out.print("First List is: ");
        FileProcessor.printList(list1);
        System.out.println(lineSeparator());

        int n = 4;
        System.out.print("Exponent: ");
        System.out.print(n);
        System.out.println(lineSeparator());

        System.out.print("Result: ");
        Node result = Calculations.Exponentiation(list1, n);
        FileProcessor.printList(result);
    }
    @Test
    public void Test_Expo1 () {
        Node list1 = new Node(2, null);
        list1.next = new Node(1, null);
        int n = 2;

        Node result = new Node(4, null);
        result.next = new Node(4, null);
        result.next.next = new Node(1, null);

        assertTrue(result.equals(Calculations.Exponentiation(list1, n)));
    }
    @Test
    public void Test_Expo2 () {
        Node list1 = new Node(2, null);
        int n = 10;

        Node result = new Node(4, null);
        result.next = new Node(2, null);
        result.next.next = new Node(0, null);
        result.next.next.next = new Node(1, null);

        assertTrue(result.equals(Calculations.Exponentiation(list1, n)));
    }
}
