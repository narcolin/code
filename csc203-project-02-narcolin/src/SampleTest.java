import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;

import static java.lang.System.lineSeparator;
import static org.junit.Assert.*;

/**
 * This file contains JUnit tests for some sample arithmetic
 * expressions. This file tests your program "as a whole", by
 * checking its printed output.
 *
 * YOU SHOULD NOT WRITE YOUR OWN TESTS THIS WAY, OR IN THIS FILE.
 * You should test the individual UNITS in your program, i.e., call
 * your add, multiply, and exponentiate methods and test their return
 * values.
 */
public class SampleTest {
    /**
     * The actual standard output stream.
     */
    private PrintStream old;

    /**
     * The streams we're using to capture printed output.
     */
    private ByteArrayOutputStream baos;

    /**
     * Gets called before each test method. Need to do this so that we can
     * capture the printed output from each method.
     */
    @Before
    public void setUp() {
        this.old = System.out; // Save a reference to the original stdout stream.
        this.baos = new ByteArrayOutputStream();
        PrintStream ps = new PrintStream(baos);
        System.setOut(ps);
    }

    @Test
    public void testSampleFile() {
        Main.main(new String[] { "SampleInput.txt" });
        String output = this.baos.toString();
        assertEquals("1 + 2 = 3" + lineSeparator() +
                "2 ^ 4 = 16" + lineSeparator() +
                "3 * 5 = 15" + lineSeparator() +
                "2 ^ 40 = 1099511627776" + lineSeparator(), output);
    }
    @Test
    public void testSampleFile1() {
        Main.main(new String[] {"SampleInput1.txt"});
        String output = this.baos.toString();
        assertEquals("9301 + 77 = 9378" + lineSeparator() +
                "9 ^ 3 = 729" + lineSeparator() +
                "8 * 34 = 302" + lineSeparator() +
                "200 * 3 = 600" + lineSeparator() +
                "109 + 30 = 139" + lineSeparator() +
                "12 ^ 2 = 144" + lineSeparator() +
                "3800 * 2 = 7600" + lineSeparator(), output);
    }
        /**
         * Gets called after each test method. Need to do this so that we are
         * no longer capturing all printed output and printed stuff appears
         * like normal.
         */
        @After
        public void tearDown () {
            System.out.flush();
            System.setOut(this.old);
        }
    }
