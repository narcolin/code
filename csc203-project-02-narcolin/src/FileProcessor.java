import java.awt.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileProcessor {
    /**
     * Processes arithmetic expressions line-by-line in the given file.
     *
     * @param filePath Path to a file containing arithmetic expressions.
     */
    public static void processFile(String filePath) {
        File infile = new File(filePath);
        try (Scanner scan = new Scanner(infile).useDelimiter("\\s*")) {
            while (scan.hasNext()) {
                String line = scan.nextLine();
                if (!line.equals("")) {
                    String[] split_line = line.split("\\s+");
                    Node num1 = intToNode(Integer.parseInt(split_line[0]));
                    String operator = split_line[1];
                    Node num2 = null;
                    Node result = null;
                    if (operator.equals("+")) {
                        num2 = intToNode(Integer.parseInt(split_line[2]));
                        result = Calculations.Addition(num1, num2);
                        printList(num1);
                        System.out.print(" + ");
                        printList(num2);
                        System.out.print(" = ");
                        printList(result);
                    } else if (operator.equals("*")) {
                        num2 = intToNode(Integer.parseInt(split_line[2]));
                        result = Calculations.Multiplication(num1, num2);
                        printList(num1);
                        System.out.print(" * ");
                        printList(num2);
                        System.out.print(" = ");
                        printList(result);
                    } else if (operator.equals("^")) {
                        int number2 = Integer.parseInt(split_line[2]);
                        result = Calculations.Exponentiation(num1, number2);
                        printList(num1);
                        System.out.print(" ^ ");
                        System.out.print(number2);
                        System.out.print(" = ");
                        printList(result);
                    }
//                System.out.println(scan.nextLine());
                    // TODO: Process each line of the input file here.
//                String line = scan.nextLine();
//                System.out.println(line);
                    System.out.println("");
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + infile.getPath());
        }
    }

    public static Node intToNode(int num) {
        String num_str = String.valueOf(num);
        Node result = null;

        for (int i = 0; i < num_str.length(); i++) {
            result = new Node(Integer.parseInt(num_str.substring(i, i+1)), result);
        }
        return result;
    }

    public void readLine(String filePath){
        try{
            Scanner scanner = new Scanner(new File(filePath));
            while (scanner.hasNextLine()) {
                Node num1 = intToNode(scanner.nextInt());
                String operator = scanner.next();
                Node num2 = null;
                Node result = null;
                switch (operator) {
                    case "+":
                        num2 = intToNode(scanner.nextInt());
                        result = Calculations.Addition(num1, num2);
                        printList(num1);
                        System.out.print(" + ");
                        printList(num2);
                        System.out.print(" = ");
                        printList(result);
                    case "*":
                        num2 = intToNode(scanner.nextInt());
                        result = Calculations.Multiplication(num1, num2);
                        printList(num1);
                        System.out.print(" * ");
                        printList(num2);
                        System.out.print(" = ");
                        printList(result);
                    case "^":
                        int number2 = scanner.nextInt();
                        result = Calculations.Exponentiation(num1, number2);
                        printList(num1);
                        System.out.print(" ^ ");
                        System.out.print(number2);
                        System.out.print(" = ");
                        printList(result);
                }
                System.out.println(scanner.nextLine());
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    public static void printList(Node printNode) {
        Node nxt = printNode;
        String number = "";
        while (nxt != null) {
            number = nxt.digit + number;
            nxt = nxt.next;
        }
        System.out.print(number);
    }
                 //split line into num1 num1 and operator
//            }
//    }
}
